# PAR Overview 
Preservation Action Registries (PAR) has been set up to address a set of fundamental issues that affect the digital preservation (DP) community namely to:

* facilitate the sharing of preservation actions between disparate DP systems, and
* provide the ability for well formed preservation workflows, including sets of compounded preservation workflows to be imported and used within local environments from one or more external trusted sources

Typically, proprietary DP systems lack a common means to describe and execute preservation policies and actions. For example, Archivematica’s Format Policy Register (FPR) and Preservica’s Linked Data Registry (LDR) both define what tools and rules to use to execute specific DP actions but they are not interoperable. In a nutshell:

* The two solutions cannot share technical information thereby making it difficult for users to share experiences, learnings and good practice

The aim of PAR is to overcome this problem by providing the means to connect different registries to exchange policy information about preservation actions. The model makes registry content accessible through a feature rich API using a distributed set of registries. In this way information can be made available from a range of source registries as well as via direct exchange between trusted peer institutions or systems. 

# PAR Today
Following some initial funding from Jisc, PAR has evolved from a standing start to a standalone entity using the expertise and resources of a set of industry leading organisations to form the nucleus of the PAR core team

* Preservica
* Actefactual
* Archivum
* Open Preservation Forum

To add further credibility, Wikidp is in the process of connecting into the network as a significant trusted source partner. The core team is currently in discussion with other potential sources to expand the network over the course of the coming months. 

As of April 2020, the OPF became the overall custodians of PAR with the aim of shifting the emphasis to create a more community focused program to help define development priorities as well as fostering community contribution.     

The core software (v0.3) is still at pre production stage and needs to evolve significantly before it is generally available. The high level roadmap for PAR is outlined in the Roadmap section. At present the core components comprise:

* feature rich API - see Resources
* Endpoint browser
* Prototype implementation spanning Preservica, Achivematica and Arkivum DP systems

# The PAR Vision
The PAR vision is based on the establishment of a set of trusted sources that would provide the catalyst for information and good practice sharing across a set of proprietary Digital Preservation systems as well as the wider community. The end user would be able to determine the best / most appropriate preservation action sequences to fulfill their needs and have the opportunity to review, select or discard those options. Trusted sources could comprise:
 
* Vendor systems
* National standards body
* Recognised trusted community sources such as wikidp
* Research institutions
* Universities etc.

It is envisaged that PAR would act as an enabler connecting users to sources of good practice allowing them to review singular, complex and compounded actions and via their own systems, proprietary applications and / or client tools elect to import those actions into their own local environments. Likewise they would have the ability to make their own complex workflows available to other members of the DP community ensuring that data is shared throughout the PAR enterprise.


<img src="/assets/img/par-model.svg" alt="PAR simplified conceptual model"/>

<img src="/assets/img/par_concept.svg" alt="PAR concept"/>


# PAR Roadmap
The priorities associated with each area of development are in the process of being further defined as is the finite detail associated with each release to move PAR from its current version, 0.3 to a production version 1.0.

The main components of the roadmap are highlighted below:

**API extensions** The existing Swagger documentation can be accessed via the Resources page. Further planned enhancements include:
* identity management
* what else?
* what else 

**Sync tool** that will:
* enable preservation actions to be copied between systems??
* What else?
* c

**Registry browser** this will replace the existing prototype, key functions will include:
* What else?
* b
* c  

**Register editing tool**
* This will enable users to update their registry??
* What else?
* b

**Client GUI tool**
* a
* c
* c

Would be nice to include some kind of plan / pictorial view of development ordering even if there are no timelines




# Community Contribution
Following the transfer of the PAR stewardship to the OPF the focus has to be to educate and engage the community with the concepts of PAR and in doing so to encourage greater community involvement. Specifically we are looking towards the community to help with:

* Product development - those with Java, REST API and JSON schema development skills would be of particular interest
* Documentation development - production of user guides and release notes

In addition we would particularly welcome contribution from:

* Trusted sources - those that are able to become an integral part of the PAR network by connecting their source registry’s
* DP system vendors - that would be interested in participating in and extending the PAR DP vendor network 

# How to get Involved
Product and documentation development tasks are contained in the Github repo: https://github.com/openpreserve/par. 

## Development Contribution
1. Sign up for Github
2. Request OPF to assign you to the PAR community development team
3. Review the Issues log; select Issues that have a current release milestone 
4. If there is an Issue you want to work on that does not have any associated milestone please contact OPF
5. Select Issues that are labelled as ‘Community Issue’
6. Assign yourself to the Issue! 

PAR team question - how will this process be managed? Do we hold monthly community calls to check progress / encourage input. Do we advertise these?? We need to agree a process

## Logging an Issue
1. a
2. b
3. c




# PAR Resources

The following PAR resources are available for reference / context:

## API Swagger Documentation
* xxx

## Presentations and Background Material
* PAR 2020 Webinar v01 310320 (1).pdf
* PAR Presentation York 2019.pdf
* PAR Presentation iPres 2019.pdf
* PAR Presentation iPres 2018.pdf

## Other PAR resources
* GitHub Repository
* Project Announcement

# Contacts
Please direct any PAR questions / queries to any of the par core team below:

## Open Preservation Forum
* Organisational / planning - Martin Speller; martin.speller@openpreservation.org
* Technical, specialism PAR client GUI - Carl Wilson; carl.wilson@openpreservation.org

## Preservica
* Technical, specialism registry browser  - Jon Tilbury; jonathan.tilbury@preservica.com
* Technical, specialism PAR API- Jack OSullivan; jack.osullivan@preservica.com 

## Arkivum
* Technical, specialism ??? - Matthew Addis; matthew.addis@arkivum.com 

## Artefactual
* Technical, specialism ???? - Justin Simpson; jsimpson@artefactual.com 


