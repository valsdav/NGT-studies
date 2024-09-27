# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Phase2 -s L1,L1TrackTrigger,L1P2GT --processName=SKIM --conditions auto:phase2_realistic_T33 --geometry Extended2026D110 --era Phase2C17I13M9 --eventcontent FEVTDEBUGHLT --datatier GEN-SIM-DIGI-RAW-MINIAOD --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2FEVTDEBUGHLT.customisePhase2FEVTDEBUGHLT,L1Trigger/Configuration/customisePhase2TTOn110.customisePhase2TTOn110 --filein file:/eos/cms/store/relval/CMSSW_14_1_0_pre6/RelValMinBias_14TeV/GEN-SIM-DIGI-RAW/PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v3/2560000/005fa022-76e5-4eef-8909-2678cca4152b.root --fileout file:output_Phase2_L1T.root --python_filename rerunL1_L1ASkim_cfg_14_2_0_pre1.py --inputCommands=keep *, drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT --outputCommands=drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT --mc -n -1 --nThreads 12 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9

process = cms.Process('SKIM',Phase2C17I13M9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D110Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimPhase2L1GlobalTriggerEmulator_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.prototypeSeeds')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


# Get VarParsing
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
# read an input argument
options.register ('inputFile',
                    0,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.int,
                    "Input file to process")
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

from list_cff_ttbar_Spring24_Phase2_PU import inputFileNames
# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(inputFileNames[options.inputFile]),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop l1tPFJets_*_*_*',
        'drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Phase2 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
myOutputCommands = cms.untracked.vstring(
        'drop *_*_*_HLT',
        'drop *_*_*_RECO',
        'drop *_*_*_SIM',
        'drop triggerTriggerFilterObjectWithRefs_l1t*_*_HLT',
        'keep FEDRawDataCollection_rawDataCollector_*_HLT',
        'keep *_simSiPixelDigis_*_*',
        'keep Phase2TrackerDigiedmDetSetVector_*_*_HLT',
        'keep *_simMuonRPCDigis_*_HLT',
        'keep *_*_bunchSpacing_HLT',
        'keep *_mix_FTL*_HLT',
        'keep *_mix_EBTimeDigi_HLT',
        'keep *_simHGCalUnsuppressedDigis_*_HLT',
        'keep *_simMuonCSCDigis_*_HLT',
        'keep *_simMuonDTDigis_*_HLT',
        'keep *_simMuonGEMDigis_*_HLT',
        'keep *_*_*_SKIM'
        )


process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:output_Phase2_L1T_' + str(options.inputFile) + '.root'),
    outputCommands = myOutputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T33', '')
process.FEVTDEBUGHLToutput.outputCommands.append('drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT')

# Path and EndPath definitions
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger)
process.Phase2L1GTProducer = cms.Path(process.l1tGTProducerSequence)
process.Phase2L1GTAlgoBlockProducer = cms.Path(process.l1tGTAlgoBlockProducerSequence)
process.TripleTkMuon_5_3_0_DoubleTkMuon_5_3_OS_MassTo9 = cms.Path(process.TripleTkMuon530OSMassMax9)
process.TripleTkMuon_5_3p5_2p5_OS_Mass5to17 = cms.Path(process.TripleTkMuon53p52p5OSMass5to17)
process.pDoubleEGEle37_24 = cms.Path(process.DoubleEGEle3724)
process.pDoubleIsoTkPho22_12 = cms.Path(process.DoubleIsoTkPho2212)
process.pDoublePuppiJet112_112 = cms.Path(process.DoublePuppiJet112112)
process.pDoublePuppiJet160_35_mass620 = cms.Path(process.DoublePuppiJet16035Mass620)
process.pDoublePuppiTau52_52 = cms.Path(process.DoublePuppiTau5252)
process.pDoubleTkEle25_12 = cms.Path(process.DoubleTkEle2512)
process.pDoubleTkElePuppiHT_8_8_390 = cms.Path(process.DoubleTkElePuppiHT)
process.pDoubleTkMuPuppiHT_3_3_300 = cms.Path(process.DoubleTkMuPuppiHT)
process.pDoubleTkMuPuppiJetPuppiMet_3_3_60_130 = cms.Path(process.DoubleTkMuPuppiJetPuppiMet)
process.pDoubleTkMuon15_7 = cms.Path(process.DoubleTkMuon157)
process.pDoubleTkMuonTkEle5_5_9 = cms.Path(process.DoubleTkMuonTkEle559)
process.pDoubleTkMuon_4_4_OS_Dr1p2 = cms.Path(process.DoubleTkMuon44OSDr1p2)
process.pDoubleTkMuon_4p5_4p5_OS_Er2_Mass7to18 = cms.Path(process.DoubleTkMuon4p5OSEr2Mass7to18)
process.pDoubleTkMuon_OS_Er1p5_Dr1p4 = cms.Path(process.DoubleTkMuonOSEr1p5Dr1p4)
process.pIsoTkEleEGEle22_12 = cms.Path(process.IsoTkEleEGEle2212)
process.pNNPuppiTauPuppiMet_55_190 = cms.Path(process.NNPuppiTauPuppiMet)
process.pPuppiHT400 = cms.Path(process.PuppiHT400)
process.pPuppiHT450 = cms.Path(process.PuppiHT450)
process.pPuppiMET200 = cms.Path(process.PuppiMET200)
process.pPuppiMHT140 = cms.Path(process.PuppiMHT140)
process.pPuppiTauTkIsoEle45_22 = cms.Path(process.PuppiTauTkIsoEle4522)
process.pPuppiTauTkMuon42_18 = cms.Path(process.PuppiTauTkMuon4218)
process.pQuadJet70_55_40_40 = cms.Path(process.QuadJet70554040)
process.pSingleEGEle51 = cms.Path(process.SingleEGEle51)
process.pSingleIsoTkEle28 = cms.Path(process.SingleIsoTkEle28)
process.pSingleIsoTkPho36 = cms.Path(process.SingleIsoTkPho36)
process.pSinglePuppiJet230 = cms.Path(process.SinglePuppiJet230)
process.pSingleTkEle36 = cms.Path(process.SingleTkEle36)
process.pSingleTkMuon22 = cms.Path(process.SingleTkMuon22)
process.pTkEleIsoPuppiHT_26_190 = cms.Path(process.TkEleIsoPuppiHT)
process.pTkElePuppiJet_28_40_MinDR = cms.Path(process.TkElePuppiJetMinDR)
process.pTkEleTkMuon10_20 = cms.Path(process.TkEleTkMuon1020)
process.pTkMuPuppiJetPuppiMet_3_110_120 = cms.Path(process.TkMuPuppiJetPuppiMet)
process.pTkMuTriPuppiJet_12_40_dRMax_DoubleJet_dEtaMax = cms.Path(process.TkMuTriPuppiJetdRMaxDoubleJetdEtaMax)
process.pTkMuonDoubleTkEle6_17_17 = cms.Path(process.TkMuonDoubleTkEle61717)
process.pTkMuonPuppiHT6_320 = cms.Path(process.TkMuonPuppiHT6320)
process.pTkMuonTkEle7_23 = cms.Path(process.TkMuonTkEle723)
process.pTkMuonTkIsoEle7_20 = cms.Path(process.TkMuonTkIsoEle720)
process.pTripleTkMuon5_3_3 = cms.Path(process.TripleTkMuon533)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.L1simulation_step,process.L1TrackTrigger_step,process.Phase2L1GTProducer,process.Phase2L1GTAlgoBlockProducer,process.TripleTkMuon_5_3_0_DoubleTkMuon_5_3_OS_MassTo9,process.TripleTkMuon_5_3p5_2p5_OS_Mass5to17,process.pDoubleEGEle37_24,process.pDoubleIsoTkPho22_12,process.pDoublePuppiJet112_112,process.pDoublePuppiJet160_35_mass620,process.pDoublePuppiTau52_52,process.pDoubleTkEle25_12,process.pDoubleTkElePuppiHT_8_8_390,process.pDoubleTkMuPuppiHT_3_3_300,process.pDoubleTkMuPuppiJetPuppiMet_3_3_60_130,process.pDoubleTkMuon15_7,process.pDoubleTkMuonTkEle5_5_9,process.pDoubleTkMuon_4_4_OS_Dr1p2,process.pDoubleTkMuon_4p5_4p5_OS_Er2_Mass7to18,process.pDoubleTkMuon_OS_Er1p5_Dr1p4,process.pIsoTkEleEGEle22_12,process.pNNPuppiTauPuppiMet_55_190,process.pPuppiHT400,process.pPuppiHT450,process.pPuppiMET200,process.pPuppiMHT140,process.pPuppiTauTkIsoEle45_22,process.pPuppiTauTkMuon42_18,process.pQuadJet70_55_40_40,process.pSingleEGEle51,process.pSingleIsoTkEle28,process.pSingleIsoTkPho36,process.pSinglePuppiJet230,process.pSingleTkEle36,process.pSingleTkMuon22,process.pTkEleIsoPuppiHT_26_190,process.pTkElePuppiJet_28_40_MinDR,process.pTkEleTkMuon10_20,process.pTkMuPuppiJetPuppiMet_3_110_120,process.pTkMuTriPuppiJet_12_40_dRMax_DoubleJet_dEtaMax,process.pTkMuonDoubleTkEle6_17_17,process.pTkMuonPuppiHT6_320,process.pTkMuonTkEle7_23,process.pTkMuonTkIsoEle7_20,process.pTripleTkMuon5_3_3,process.endjob_step,process.FEVTDEBUGHLToutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


l_pathname = [
'pDoubleEGEle37_24',
'pDoubleIsoTkPho22_12',
'pDoublePuppiJet112_112',
'pDoublePuppiJet160_35_mass620',
'pDoublePuppiTau52_52',
'pDoubleTkEle25_12',
'pDoubleTkElePuppiHT_8_8_390',
'pDoubleTkMuPuppiHT_3_3_300',
'pDoubleTkMuPuppiJetPuppiMet_3_3_60_130',
'pDoubleTkMuon15_7',
'pDoubleTkMuonTkEle5_5_9',
'pDoubleTkMuon_4_4_OS_Dr1p2',
'pDoubleTkMuon_4p5_4p5_OS_Er2_Mass7to18',
'pDoubleTkMuon_OS_Er1p5_Dr1p4',
'pIsoTkEleEGEle22_12',
'pNNPuppiTauPuppiMet_55_190',
'pPuppiHT400',
'pPuppiHT450',
'pPuppiMET200',
'pPuppiMHT140',
'pPuppiTauTkIsoEle45_22',
'pPuppiTauTkMuon42_18',
'pQuadJet70_55_40_40',
'pSingleEGEle51',
'pSingleIsoTkEle28',
'pSingleIsoTkPho36',
'pSinglePuppiJet230',
'pSingleTkEle36',
'pSingleTkMuon22',
'pTkEleIsoPuppiHT_26_190',
'pTkElePuppiJet_28_40_MinDR',
'pTkEleTkMuon10_20',
'pTkMuPuppiJetPuppiMet_3_110_120',
'pTkMuTriPuppiJet_12_40_dRMax_DoubleJet_dEtaMax',
'pTkMuonDoubleTkEle6_17_17',
'pTkMuonPuppiHT6_320',
'pTkMuonTkEle7_23',
'pTkMuonTkIsoEle7_20',
'pTripleTkMuon5_3_3'
]

l_path = []

logExpStr = None

for pathname in l_pathname :
    
    #process.load(f"HLTrigger.Configuration.HLT_75e33.paths.{pathname}_cfi")
    
    if (logExpStr is None) :
        logExpStr = pathname
    else :
        logExpStr += f" or {pathname}"
        #logExpStr += f" and {pathname}"
    # no need to run them, they are already scheduled
    #l_path.append(getattr(process, pathname))

process.L1skimFilter = cms.EDFilter("PathStatusFilter",
    logicalExpression = cms.string(logExpStr)
)

process.L1skimPath = cms.Path(process.L1skimFilter)
l_path.append(process.L1skimPath)

process.schedule.extend([*l_path])

# Add the filter in the output module
EventSelection = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring("L1skimPath")                     
    )
)


#Setup FWK for multithreaded
process.options.numberOfThreads = 2
process.options.numberOfStreams = 4

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT
from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT import customisePhase2FEVTDEBUGHLT 

#call to customisation function customisePhase2FEVTDEBUGHLT imported from L1Trigger.Configuration.customisePhase2FEVTDEBUGHLT
process = customisePhase2FEVTDEBUGHLT(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2TTOn110
from L1Trigger.Configuration.customisePhase2TTOn110 import customisePhase2TTOn110 

#call to customisation function customisePhase2TTOn110 imported from L1Trigger.Configuration.customisePhase2TTOn110
process = customisePhase2TTOn110(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
