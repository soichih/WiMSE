#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# What is the goal of this work?
# 
#     Although our ability to generate more and more plausible models of human white matter architecture via diffusion-based tractography has improved in recent years, there still remain many challenges to characterizing the mesoscale structure of such models.  This is particularly true if the goal of our characterizations is to conduct a comparison across subjects or groups.  One approach to developing such characterizations has been the segmentation of whole-brain, streamline based models, referred to as tractomes, into smaller collections of streamlines which correspond to known white matter structures.  Though it is a matter for disucssion later, its worth noting here that this is just one approach to generate a model of white matter among many.  However, it is here argued that the rapidly increasing popularity of tractography-based brain research [FIG/REF]--and white matter segmentation-based research more specifically [FIG/REF]--highlights an as-of-yet unmet need in the field: a comprehensive guide to modern, digital white matter segmentation.  This gap stands as a huge challenge for all those working on this topic.  Consequences of this gap can be observed quite readily in the field.
#     The ongoing proliferation of automated & semi-automated segmentation methods [REFs], along with the continuing popularity of manual segmentation methods [REFs], is potentially [INDICATIVE?SUGGESTIVE?] of a field with an excessively wide range of [UNSPOKEN PRESUMPTIONS].  Having these many groups working independently (or semi-independently) may be a desirable state of affairs in a nacient field such as ours, but this may also give us cause for concern.  While it is true that disparate investigators may be better able to search the model-space [REF] constituting potential approaches to white matter segmentation, this framework really only works if researchers can orient their work in a useful fashion with one another.  Unfortunately, perhaps because of the limitations of traditional publication resources [REFs] or because of the necessary opacity of code or toolbox implementations [REFs], many of the presumptions, general approaches, and conceptual frameworks underlying these approaches remain unspoken or undercharacterized.  Herein, an attempt to deal with these challenges is presented.
#     The work presented in this collection is intended to acheive two goals with one, comprehensive approach.  By taking a step back from the somewhat artisan-like approach that has taken hold in the field, wherein bespoke segmentations are produced by practitioners who have developed a raft of un- or under-documented habits, and instead approaching the field from the perspective of a relative novice, it may be possible to both provide a resource that is of genuine utiliity to newcomers *and* to engage in [SELFREFLECTIION?] of the field itself.  As an autobiographical aside, the author of this work was primarily self taught in the practices (rather than the ______) of modern digital neuroanatomy, and as such developed a host of "un- or under-documented habits" theirself.  It was only in comparing segmentation approaches during trouble-shooting and during conversations with collaborators/trainees that the artisanal nature of the work became apparent.  Thus there are two intended outcomes with this work: (1) the provision a guide for neophyte digital white matter anatomists and (2) the establishment of a communially useful conceptual framework for white matter segmentation.  To to make progress towards these intended outcomes though, we must first consider what it is we are attempting to acheive when we segment white matter.  
# 
# What is white matter segmentation?
# 
#     The process of white matter segmentation, an admittedly arcane sounding endeavor, is best understood in virtue of its goal(s).  That is, "What is white matter segmentation *actually* attempting to acheive?"  Although the collective set of researchers engaged in this work may have disparate goals, there are nonetheless threads which bind their work.  Namely, it seems reasonable to claim that what we are doing when we segment the white matter of the brain is this: we are attempting to distinguish, identify, and perhaps even characterize anatomical structures of the white matter relative to one another and to the surrounding brain tissue.  More to the point, our practical goal is to be able to engage in this process in a "consistent" fashion--whether presented with a brain featuring a neurological abnormality or a brain from a particularly young or old invidual.  "Consistent" is indeed the key word here, as it is pulling double duty in the preceeding sentence.  It is important to pull these two meanings apart because they are both essential to what we would desire of a segmentation.
#     In the first and most general sense, we can think of segmentation like any other capability, and so "consistent" in this sense would simply refer to the frequency which the aforementioned goals ("to distinguish, identify, and ... characterize") could be acheived.  A high frequency of acheiving these goals would constitute a "consistent" (i.e. on a regular basis) ability to segment the brain; given a brain (or a model thereof) it is reasonably safe to assume that we could "carve" it in a fashion that is in keeping with the aformentioned three goals.  Notably though, those three goals--at least insofar as they are presented above--are not sufficient to guarentee that a comparison could be made across subjects, or indeed, even within individual subjects at different time points.  It would be quite possible and sensible to segment one brain into two hemispheres, and then to segment another into several dozen meaningful components, and yet we may be quite unsatisfied with this segmentation ability.  Because we were able to segment all (both) brains, and never failed to segment any particular brain, our segmentation ability was entirely "consistent", but this probably wouldn't constitute a useful segmentation capibility.  For this, we would need to be able to segment "consistently" in another sense.
#     The ability to use a segmentation to make comparisons across subjects necessiates that the elements that the segmentaton carves the brain into be, in some meaningful sense, "the same".  That is, these constituitive components somehow correspond to one another.  "Consistent", in this sense, characterizes the ability of a segmentation to *accurately* identify sub-components of the brain as being instances of the same over-arching category (i.e. brainstem).  Notably though, this entails nothing about the frequency with which the process of segmentation can actually be engaged in.  A segmentation could still be considered "consistent" in this sense even if it failed in half the cases.  So long as we can be certian that, if the segmentation succeeds, then the segmented elements are appropriately isomorphic [REF] to one another, it would meet this criteria.  Here, what we are concerned with is the ability to identify structures of the brain that are homologous [REF] to one another.  Within the context of a research setting, even if a segmentation method is wholly consistent in this isomorphism-mapping sense, it still may not be useful if it can't be implimented on a sufficient number of subjects.  
#     
# How has segmentation been done?
#     
#     This is not unlike the process of using a resource like Gray's Anatomy [REF] to identify parts of a given body.  Old as that resource may be, its insights are still perfectly useful and valid to this day.  Similarly, even as we engage in the study and segmentation of white matter in the 21st century, we can and often do find ourselves making references to work done centuries ago.  Indeed, a quick consideration of the way that historical white matter work was done can help contextualize why and how we do things the way we do today.
# 
# [historical background]. Having considered our historical predecessors, we can now shift our attention to our our own anatomical work and adress a question that should surely be  
#     
#     Granted, there are a number of characteristics that distinguish that process from the process of white matter segmentation that we'll examine, but for now the whole body analogy at least provides an idea of our overarching goals.
#         
# Why is this an iPython notebook, and not just a standard document?
#     
#     of cortical segmentation conducted most notably by Freesurfer, as well as a number of other methodologies.  A consideration of the characteristics of a cortical segmentation can provide a useful basis for comparison.

# In[ ]:





# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Building intuitions with digital images
# 
# Why_are_we_talking_about_JPEGs
# Intro_to_discretized_image_representation_&_maps
# Aligning_two_images
# Multi_object_maps_in_images
# A_consideration_of_jpegs_and_brain_images
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Working with NIfTI data
# 
# How_to_represent_the_brain's_anatomy_-_as_a_volume
# A_quick_demonstration_of_linear_affine_transformations_in_3-D
# How_to_interpret_a_volumetric_brain_segmentation
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: White matter and tractography
# 
# Highways_of_the_brain
# The_measurement,_the_object,_and_the_modality_-_What's_measured_in_diffusion_imaging
# The_voxel_and_the_streamline
# The_source_tractogram
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Segmenting tractography
# 
# A_first_segmentation
# ```
# 
