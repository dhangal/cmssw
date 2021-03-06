from RecoVertex.AdaptiveVertexFinder.inclusiveVertexing_cff import *
from RecoBTag.CSVscikit.csvscikit_cff import *

# new candidate-based ctagging sequence, requires its own IVF vertices (relaxed IVF reconstruction cuts)
# but IP and soft-lepton taginfos from btagging sequence can be recycled
pfCSVscikit = cms.Sequence(
#   ( #inclusiveCandidateVertexingCvsL *
      #pfInclusiveSecondaryVertexFinderCvsLTagInfos
#   )

    # CSV + soft-lepton variables combined (ctagger optimized for c vs dusg)
    #* pfCombinedCvsBJetTags
    #* pfCombinedCvsLJetTags
    
#    * pfCSVscikitJetTags
   # * pfCSVscikitDummy

   pfCSVscikitJetTags
)
