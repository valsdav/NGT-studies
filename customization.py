from HLTrigger.Configuration.common import *
from FWCore.ParameterSet.Modules import *
from FWCore.ParameterSet.Config import *
from FWCore.ParameterSet.SequenceTypes import *


from rich import print

def remove_path(process, path):
    if hasattr(process, path):
        print(f"- [green]Removing path {path}")
        delattr(process, path)
    else:
        print(f"- [red]Path {path} not found")
        
    if hasattr(process, 'PrescaleService'):
        # if prescale service is present, remove the prescale for the path
        for pset in process.PrescaleService.prescaleTable:
            if pset.pathName.value() == path:
                process.PrescaleService.prescaleTable.remove(pset)


def remove_paths_from_dataset(process, dataset, filter_str=None):
    for module in getattr(process, dataset).moduleNames():
        if isinstance(getattr(process, module), cms.EDFilter) and getattr(process, module).type_() == 'TriggerResultsFilter':
            print("[blue] Removing filters part of dataset: ", dataset)
            for filter_ in getattr(process, module).triggerConditions:
                filter_name = filter_.split("/")[0].strip()
                if filter_str and filter_str not in filter_name:
                    continue
                remove_path(process, filter_name)
            print("--------------")


def find_paths_of_module(process, module_name):
    paths = []
    for path in process.paths:
        if module_name in process.paths[path].moduleNames():
            paths.append(path)
    return paths

def find_datasets_of_path(process, path_name):
    datasets = []
    for name, path in process.paths.items():
        if name.startswith('Dataset_'):
            for module in path.moduleNames():
                if isinstance(getattr(process, module), cms.EDFilter) and getattr(process, module).type_() == 'TriggerResultsFilter':
                    if path_name in getattr(process, module).triggerConditions:
                        datasets.append(name)
    return datasets
       
            
def disable_filters(process, verbose=False):
    for path_label, path in process.paths.items():
        for module in path.moduleNames():
            module_obj= getattr(process, module)
            if isinstance(module_obj, cms.EDFilter):
                # Exclude some of the filters
                if module in ['hltBoolEnd', 'hltBoolFalse','hltTriggerType']:
                    continue
                if module_obj.type_() == 'HLTL1TSeed':
                    continue
                if "L1TPreFilter" in module_obj.type_():
                    continue
                if "L1TMatchFilterRegional" in module_obj.type_():
                    continue
                if module_obj.type_() == 'TauTagFilter':
                    continue
                # What to do with HLTPrescaler used for L1T objects?
                    
                if verbose:
                    print("[orange]Ignoring filter: ", module)
                # we replace the module with a cms.ignore
                path.replace(module_obj,  cms.ignore(module_obj))
    

def customizeForProfiling(process, ignore_filters=False):
    # simplify the menu for timing studies
    #process.hltDatasetCommissioning.triggerConditions.remove('HLT_PFJet40_GPUvsCPU_v3')
    # Removing paths
    remove_paths_from_dataset(process, 'Dataset_ScoutingPFMonitor', filter_str='PFScouting')
    remove_path(process, 'Dataset_ScoutingPFMonitor')
    remove_path(process, 'PhysicsScoutingPFMonitorOutput')
    remove_path(process, 'Dataset_OnlineMonitor')
    remove_path(process, 'Dataset_Commissioning')
    remove_path(process, 'DQMOutput')

    with open('metadata/paths_alca.txt', 'r') as paths_alca:
        for path in paths_alca:
            remove_path(process, path.strip())


    with open('metadata/paths_parking.txt', 'r') as paths_parking:
        for path in paths_parking:
            remove_path(process, path.strip())

    with open('metadata/paths_scouting.txt', 'r') as paths_scouting:
        for path in paths_scouting:
            remove_path(process, path.strip())

    # Remove Alca paths
    print("Removing AlCa paths")
    for path in process.paths:
        if 'AlCa' in path:
            remove_path(process, path)
            
    # Remove DQM paths
    print("Removing DQM paths")
    for path in process.paths:
        if 'DQM' in path:
            remove_path(process, path)

    # Remove MC paths
    remove_paths_from_dataset(process, 'Dataset_MonteCarlo')
    remove_path(process, 'Dataset_MonteCarlo')

    if hasattr(process, 'hltOutputDQMGPUvsCPU'):
        del process.hltOutputDQMGPUvsCPU

    print("Remove Parking paths")
    for path in process.paths:
        if path.startswith('Dataset_Parking'):
            remove_paths_from_dataset(process, path)
            remove_path(process, path)

    print("Remove OutputModules")
    with open("metadata/outputmodules.txt", "r") as outputmodules:
        for outputmodule in outputmodules:
            if hasattr(process, outputmodule.strip()):
                print(f"- [green]Removing output module {outputmodule.strip()}")
                delattr(process, outputmodule.strip())
            else:
                print(f"- [red]Output module {outputmodule.strip()} not found")

    if ignore_filters:
        # Disabling filters
        disable_filters(process)
    
    return process


