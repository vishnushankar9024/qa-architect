# Enriched Business Rules

Total rules: 630
Average testing value score: 8.59
CRUD reduction: 91.94%

## Collaboration and Communication

### EBR-0001

Closurecomment collaboration must keep messages and notifications linked to the related business record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.77
Source Rule IDs: BR-896
Evidence: Generated from business-rules.json rule BR-896
Tags: state transition, business, collaboration, communication, closurecomment, must, keep, messages, notifications, linked, related, record

### EBR-0002

The system must maintain Thread records as source data for Thread.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-922
Evidence: Generated from business-rules.json rule BR-922
Tags: validation, data, collaboration, communication, system, must, maintain, thread, records, source

### EBR-0003

Addparticipantstothread collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-894
Evidence: Generated from business-rules.json rule BR-894
Tags: notification, business, collaboration, communication, addparticipantstothread, must, keep, messages, notifications, linked, related, record

### EBR-0004

Chat collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-895
Evidence: Generated from business-rules.json rule BR-895
Tags: notification, business, collaboration, communication, chat, must, keep, messages, notifications, linked, related, record

### EBR-0005

Collaboration threads must preserve comments and attachments with the related business record.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.78
Source Rule IDs: BR-893, BR-894, BR-895, BR-896, BR-897, BR-898, BR-899, BR-900, BR-901, BR-902, BR-903, BR-904, BR-905, BR-906, BR-907, BR-908, BR-909, BR-910, BR-912, BR-914, BR-915, BR-916, BR-917, BR-921, BR-922, BR-923, BR-925, BR-927, BR-928, BR-929
Evidence: Feature: Addparticipantstothread Management; APIs: POST /add-participants-to-thread; Feature: Chat Management; APIs: GET /chat/:threadId, GET /chat/messages, POST /chat/evaluator-send, POST /chat/manager-send; Feature: Closurecomment Management; APIs: POST /closure-comment; Feature: Comment Management; APIs: POST /comment; Feature: Markthreadread Management; APIs: POST /mark-thread-read; Feature: Read Management; APIs: POST /read, POST /read/:threadId; Feature: Thread Management; Collections: Thread; Feature: Threadattachment Management; Collections: ThreadAttachment; Feature: Updatethreaddetail Management; APIs: POST /update-thread-details; Feature: Updatethreadtitle Management; APIs: POST /update-thread-title
Tags: audit, collaboration

### EBR-0006

Comment collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-897
Evidence: Generated from business-rules.json rule BR-897
Tags: notification, business, collaboration, communication, comment, must, keep, messages, notifications, linked, related, record

### EBR-0007

Emailnotificationlog collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-898
Evidence: Generated from business-rules.json rule BR-898
Tags: notification, business, collaboration, communication, emailnotificationlog, must, keep, messages, notifications, linked, related, record

### EBR-0008

Markthreadread collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-899
Evidence: Generated from business-rules.json rule BR-899
Tags: notification, business, collaboration, communication, markthreadread, must, keep, messages, notifications, linked, related, record

### EBR-0009

Message collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-900
Evidence: Generated from business-rules.json rule BR-900
Tags: notification, business, collaboration, communication, message, must, keep, messages, notifications, linked, related, record

### EBR-0010

Notification collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-901
Evidence: Generated from business-rules.json rule BR-901
Tags: notification, business, collaboration, communication, must, keep, messages, notifications, linked, related, record

### EBR-0011

Notifications must be generated on workflow state changes.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.82
Source Rule IDs: BR-894, BR-895, BR-896, BR-897, BR-898, BR-899, BR-900, BR-901, BR-902, BR-903, BR-904, BR-905, BR-906, BR-918, BR-919, BR-920, BR-929, BR-930, BR-931
Evidence: Feature: Emailnotificationlog Management; Collections: EmailNotificationLog; Feature: Message Management; Collections: Message; Feature: Notification Management; APIs: GET /notifications
Tags: notification, workflow

### EBR-0012

Read collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-902
Evidence: Generated from business-rules.json rule BR-902
Tags: notification, business, collaboration, communication, read, must, keep, messages, notifications, linked, related, record

### EBR-0013

The system must maintain Email Notification Log records as source data for Emailnotificationlog.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-918
Evidence: Generated from business-rules.json rule BR-918
Tags: notification, data, collaboration, communication, system, must, maintain, email, records, source, emailnotificationlog

### EBR-0014

The system must maintain Message records as source data for Message.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-919
Evidence: Generated from business-rules.json rule BR-919
Tags: notification, data, collaboration, communication, system, must, maintain, message, records, source

### EBR-0015

The system must maintain PTCMessage records as source data for Ptcmessage.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-920
Evidence: Generated from business-rules.json rule BR-920
Tags: notification, data, collaboration, communication, system, must, maintain, ptcmessage, records, source

### EBR-0016

The system must maintain Thread Attachment records as source data for Threadattachment.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-921
Evidence: Generated from business-rules.json rule BR-921
Tags: document management, data, collaboration, communication, system, must, maintain, thread, attachment, records, source, threadattachment

### EBR-0017

Thread collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-903
Evidence: Generated from business-rules.json rule BR-903
Tags: notification, business, collaboration, communication, thread, must, keep, messages, notifications, linked, related, record

### EBR-0018

Threadattachment collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-904
Evidence: Generated from business-rules.json rule BR-904
Tags: notification, business, collaboration, communication, threadattachment, must, keep, messages, notifications, linked, related, record

### EBR-0019

Threadattachment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-893
Evidence: Generated from business-rules.json rule BR-893
Tags: document management, data, collaboration, communication, threadattachment, documents, must, created, stored, updated, through, controlled, document

### EBR-0020

Updatethreaddetail collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-905
Evidence: Generated from business-rules.json rule BR-905
Tags: notification, business, collaboration, communication, updatethreaddetail, must, keep, messages, notifications, linked, related, record

### EBR-0021

Updatethreadtitle collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-906
Evidence: Generated from business-rules.json rule BR-906
Tags: notification, business, collaboration, communication, updatethreadtitle, must, keep, messages, notifications, linked, related, record

### EBR-0022

Collaboration and Communication records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-907, BR-908, BR-909, BR-910, BR-911, BR-912, BR-913, BR-914, BR-915, BR-916, BR-917
Evidence: Consolidated 11 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0023

Collaboration and Communication records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-923, BR-924, BR-925, BR-926, BR-927, BR-928, BR-929, BR-930, BR-931
Evidence: Consolidated 9 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Configuration and Master Data

### EBR-0024

Config documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-846
Evidence: Generated from business-rules.json rule BR-846
Tags: document management, data, configuration, master, config, documents, must, created, stored, updated, through, controlled, document

### EBR-0025

The system must maintain PMWeb Special Process records as source data for Pmwebspecialprocess.

Classification: Integration
Testing Value Score: 7
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-878
Evidence: Generated from business-rules.json rule BR-878
Tags: integration, data, configuration, master, system, must, maintain, pmweb, special, process, records, source, pmwebspecialprocess

### EBR-0026

Companymaster changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-849
Evidence: Generated from business-rules.json rule BR-849
Tags: configuration, business, master, data, companymaster, changes, must, managed, through, administrative, controls

### EBR-0027

Config changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-850
Evidence: Generated from business-rules.json rule BR-850
Tags: configuration, business, master, data, config, changes, must, managed, through, administrative, controls

### EBR-0028

Configuremapping changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-851
Evidence: Generated from business-rules.json rule BR-851
Tags: configuration, business, master, data, configuremapping, changes, must, managed, through, administrative, controls

### EBR-0029

Confirmdefinition changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-852
Evidence: Generated from business-rules.json rule BR-852
Tags: configuration, business, master, data, confirmdefinition, changes, must, managed, through, administrative, controls

### EBR-0030

Definition changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-853
Evidence: Generated from business-rules.json rule BR-853
Tags: configuration, business, master, data, definition, changes, must, managed, through, administrative, controls

### EBR-0031

Departmentconfiguration changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-854
Evidence: Generated from business-rules.json rule BR-854
Tags: configuration, business, master, data, departmentconfiguration, changes, must, managed, through, administrative, controls

### EBR-0032

Function changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-855
Evidence: Generated from business-rules.json rule BR-855
Tags: configuration, business, master, data, function, changes, must, managed, through, administrative, controls

### EBR-0033

Mappingbyid changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-856
Evidence: Generated from business-rules.json rule BR-856
Tags: configuration, business, master, data, mappingbyid, changes, must, managed, through, administrative, controls

### EBR-0034

Mappingbyuserid changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-857
Evidence: Generated from business-rules.json rule BR-857
Tags: configuration, business, master, data, mappingbyuserid, changes, must, managed, through, administrative, controls

### EBR-0035

The system must maintain App Module records as source data for Appmodule.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-871
Evidence: Generated from business-rules.json rule BR-871
Tags: configuration, data, master, system, must, maintain, module, records, source, appmodule

### EBR-0036

The system must maintain Capability records as source data for Capability.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-872
Evidence: Generated from business-rules.json rule BR-872
Tags: configuration, data, master, system, must, maintain, capability, records, source

### EBR-0037

The system must maintain Company Master records as source data for Companymaster.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-873
Evidence: Generated from business-rules.json rule BR-873
Tags: configuration, data, master, system, must, maintain, company, records, source, companymaster

### EBR-0038

The system must maintain Counter records as source data for Counter.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-874
Evidence: Generated from business-rules.json rule BR-874
Tags: configuration, data, master, system, must, maintain, counter, records, source

### EBR-0039

The system must maintain Department Configuration records as source data for Departmentconfiguration.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-875
Evidence: Generated from business-rules.json rule BR-875
Tags: configuration, data, master, system, must, maintain, department, records, source, departmentconfiguration

### EBR-0040

The system must maintain Function records as source data for Function.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-876
Evidence: Generated from business-rules.json rule BR-876
Tags: configuration, data, master, system, must, maintain, function, records, source

### EBR-0041

The system must maintain Group records as source data for Group.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-877
Evidence: Generated from business-rules.json rule BR-877
Tags: configuration, data, master, system, must, maintain, group, records, source

### EBR-0042

The system must maintain Section records as source data for Section.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-879
Evidence: Generated from business-rules.json rule BR-879
Tags: configuration, data, master, system, must, maintain, section, records, source

### EBR-0043

Configuration and Master Data records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-858, BR-859, BR-860, BR-861, BR-862, BR-863, BR-864, BR-865, BR-866, BR-867, BR-868, BR-870
Evidence: Consolidated 12 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0044

Configuration and Master Data records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-847, BR-848
Evidence: Consolidated 2 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0045

Configuration and Master Data records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-869
Evidence: Consolidated 1 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0046

Configuration and Master Data records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-880, BR-881, BR-882, BR-883, BR-884, BR-885, BR-886, BR-887, BR-888, BR-889, BR-890, BR-891, BR-892
Evidence: Consolidated 13 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Document, File and Template Management

### EBR-0047

Addstagegate documents must be created, stored, or updated through controlled document processes.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-657
Evidence: Generated from business-rules.json rule BR-657
Tags: state transition, data, document, file, template, management, addstagegate, documents, must, created, stored, updated, through

### EBR-0048

Addstagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-656, BR-657, BR-658, BR-659, BR-660, BR-661, BR-662, BR-663, BR-667, BR-668, BR-669, BR-670, BR-671, BR-672, BR-673, BR-676, BR-677, BR-689, BR-690, BR-691, BR-692, BR-693, BR-694, BR-696, BR-702, BR-703, BR-712, BR-713, BR-717, BR-718, BR-719, BR-720, BR-721, BR-722, BR-723, BR-724, BR-725, BR-726, BR-733, BR-734, BR-735, BR-736, BR-737, BR-751, BR-752, BR-755, BR-756, BR-757, BR-758, BR-759
Evidence: Feature: Addstagegate Management; APIs: POST /add-stagegate/:templateId
Tags: state transition, workflow, state-transition

### EBR-0049

Alltemplatestagegate documents must be created, stored, or updated through controlled document processes.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-661
Evidence: Generated from business-rules.json rule BR-661
Tags: state transition, data, document, file, template, management, alltemplatestagegate, documents, must, created, stored, updated, through

### EBR-0050

Checklisttemplatesource records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-733
Evidence: Generated from business-rules.json rule BR-733
Tags: state transition, workflow, document, file, template, management, checklisttemplatesource, records, must, move, through, defined, states

### EBR-0051

Managersteptemplate records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-734
Evidence: Generated from business-rules.json rule BR-734
Tags: state transition, workflow, document, file, template, management, managersteptemplate, records, must, move, through, defined, states

### EBR-0052

Nonemptystagegate documents must be created, stored, or updated through controlled document processes.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-696
Evidence: Generated from business-rules.json rule BR-696
Tags: state transition, data, document, file, template, management, nonemptystagegate, documents, must, created, stored, updated, through

### EBR-0053

Nonemptystagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-656, BR-657, BR-658, BR-659, BR-660, BR-661, BR-662, BR-663, BR-667, BR-668, BR-669, BR-670, BR-671, BR-672, BR-673, BR-676, BR-677, BR-689, BR-690, BR-691, BR-692, BR-693, BR-694, BR-695, BR-696, BR-702, BR-703, BR-712, BR-713, BR-717, BR-718, BR-719, BR-720, BR-721, BR-722, BR-723, BR-724, BR-725, BR-726, BR-733, BR-734, BR-735, BR-736, BR-737, BR-742, BR-751, BR-752, BR-755, BR-756, BR-757
Evidence: Feature: Nonemptystagegate Management; APIs: GET /non-empty-stagegate/:templateId
Tags: state transition, workflow, state-transition

### EBR-0054

Removeclosureattachment documents must be created, stored, or updated through controlled document processes.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-709
Evidence: Generated from business-rules.json rule BR-709
Tags: state transition, data, document, file, template, management, removeclosureattachment, documents, must, created, stored, updated, through

### EBR-0055

Savesteptemplate records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-735
Evidence: Generated from business-rules.json rule BR-735
Tags: state transition, workflow, document, file, template, management, savesteptemplate, records, must, move, through, defined, states

### EBR-0056

Steptemplate records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-736
Evidence: Generated from business-rules.json rule BR-736
Tags: state transition, workflow, document, file, template, management, steptemplate, records, must, move, through, defined, states

### EBR-0057

Templateresponse records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-737
Evidence: Generated from business-rules.json rule BR-737
Tags: state transition, workflow, document, file, template, management, templateresponse, records, must, move, through, defined, states

### EBR-0058

Uploadclosureattachment documents must be created, stored, or updated through controlled document processes.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-728
Evidence: Generated from business-rules.json rule BR-728
Tags: state transition, data, document, file, template, management, uploadclosureattachment, documents, must, created, stored, updated, through

### EBR-0059

Uploadclosureattachment file movement must use controlled import, export, upload, or download actions.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.76
Source Rule IDs: BR-747
Evidence: Generated from business-rules.json rule BR-747
Tags: state transition, technical, document, file, template, management, uploadclosureattachment, movement, must, controlled, import, export, upload

### EBR-0060

Mandatory checklist items must be completed before workflow progression.

Classification: Validation
Testing Value Score: 9
Business Criticality: Critical
Confidence: 0.88
Source Rule IDs: BR-656, BR-658, BR-659, BR-660, BR-661, BR-662, BR-663, BR-667, BR-668, BR-669, BR-670, BR-671, BR-672, BR-673, BR-676, BR-677, BR-689, BR-690, BR-691, BR-692, BR-693, BR-694, BR-695, BR-702, BR-703, BR-712, BR-713, BR-717, BR-718, BR-719, BR-720, BR-721, BR-722, BR-723, BR-724, BR-725, BR-726, BR-733, BR-734, BR-735, BR-736, BR-737, BR-742, BR-752, BR-755, BR-756, BR-757, BR-758, BR-759, BR-763
Evidence: Feature: Checklisttemplatesource Management; APIs: GET /checklist-template-sources/:templateId
Tags: validation, checklist, mandatory, workflow

### EBR-0061

Users must select an existing Attachment record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-806
Evidence: Generated from business-rules.json rule BR-806
Tags: validation, data, document, file, template, management, users, must, select, existing, attachment, record, before

### EBR-0062

Users must select an existing Outcome record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-807
Evidence: Generated from business-rules.json rule BR-807
Tags: validation, data, document, file, template, management, users, must, select, existing, outcome, record, before

### EBR-0063

Users must select an existing Template record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-808
Evidence: Generated from business-rules.json rule BR-808
Tags: validation, data, document, file, template, management, users, must, select, existing, record, before, detail

### EBR-0064

Vendor onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-655
Evidence: Generated from business-rules.json rule BR-655
Tags: validation, workflow, document, file, template, management, vendor, onboarding, must, completed, before, active, participation

### EBR-0065

Addtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-658
Evidence: Generated from business-rules.json rule BR-658
Tags: document management, data, document, file, template, management, addtemplate, documents, must, created, stored, updated, through

### EBR-0066

Allformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-659
Evidence: Generated from business-rules.json rule BR-659
Tags: document management, data, document, file, template, management, allformtemplate, documents, must, created, stored, updated, through

### EBR-0067

Alltemplateprocess documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-660
Evidence: Generated from business-rules.json rule BR-660
Tags: document management, data, document, file, template, management, alltemplateprocess, documents, must, created, stored, updated, through

### EBR-0068

Alltemplatesubactivity documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-662
Evidence: Generated from business-rules.json rule BR-662
Tags: document management, data, document, file, template, management, alltemplatesubactivity, documents, must, created, stored, updated, through

### EBR-0069

Alltemplatetask documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-663
Evidence: Generated from business-rules.json rule BR-663
Tags: document management, data, document, file, template, management, alltemplatetask, documents, must, created, stored, updated, through

### EBR-0070

Attachment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-665
Evidence: Generated from business-rules.json rule BR-665
Tags: document management, data, document, file, template, management, attachment, documents, must, created, stored, updated, through

### EBR-0071

Attachmentcomment collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-738
Evidence: Generated from business-rules.json rule BR-738
Tags: notification, business, document, file, template, management, attachmentcomment, collaboration, must, keep, messages, notifications, linked

### EBR-0072

Attachmentcomment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-666
Evidence: Generated from business-rules.json rule BR-666
Tags: document management, data, document, file, template, management, attachmentcomment, documents, must, created, stored, updated, through

### EBR-0073

Blueprinttemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-667
Evidence: Generated from business-rules.json rule BR-667
Tags: document management, data, document, file, template, management, blueprinttemplate, documents, must, created, stored, updated, through

### EBR-0074

Checklisttemplatesource documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-668
Evidence: Generated from business-rules.json rule BR-668
Tags: document management, data, document, file, template, management, checklisttemplatesource, documents, must, created, stored, updated, through

### EBR-0075

Collaboration threads must preserve comments and attachments with the related business record.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.78
Source Rule IDs: BR-664, BR-665, BR-666, BR-684, BR-708, BR-709, BR-716, BR-727, BR-728, BR-738, BR-739, BR-746, BR-747, BR-753, BR-754, BR-762, BR-772, BR-773, BR-778, BR-787, BR-788, BR-806
Evidence: Feature: Attachmentcomment Management; APIs: POST /attachment-comment; Feature: Respondattachmentcomment Management; APIs: POST /respond-attachment-comment
Tags: audit, collaboration

### EBR-0076

Collapsealltemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-669
Evidence: Generated from business-rules.json rule BR-669
Tags: document management, data, document, file, template, management, collapsealltemplate, documents, must, created, stored, updated, through

### EBR-0077

Copyformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-670
Evidence: Generated from business-rules.json rule BR-670
Tags: document management, data, document, file, template, management, copyformtemplate, documents, must, created, stored, updated, through

### EBR-0078

Copytemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-671
Evidence: Generated from business-rules.json rule BR-671
Tags: document management, data, document, file, template, management, copytemplate, documents, must, created, stored, updated, through

### EBR-0079

Createformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-672
Evidence: Generated from business-rules.json rule BR-672
Tags: document management, data, document, file, template, management, createformtemplate, documents, must, created, stored, updated, through

### EBR-0080

Createtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-673
Evidence: Generated from business-rules.json rule BR-673
Tags: document management, data, document, file, template, management, createtemplate, documents, must, created, stored, updated, through

### EBR-0081

Deletefile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-675
Evidence: Generated from business-rules.json rule BR-675
Tags: document management, data, document, file, template, management, deletefile, documents, must, created, stored, updated, through

### EBR-0082

Deleteformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-677
Evidence: Generated from business-rules.json rule BR-677
Tags: document management, data, document, file, template, management, deleteformtemplate, documents, must, created, stored, updated, through

### EBR-0083

Document documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-678
Evidence: Generated from business-rules.json rule BR-678
Tags: document management, data, document, file, template, management, documents, must, created, stored, updated, through, controlled

### EBR-0084

Documentmanager documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-679
Evidence: Generated from business-rules.json rule BR-679
Tags: document management, data, document, file, template, management, documentmanager, documents, must, created, stored, updated, through

### EBR-0085

Downloadfile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-680
Evidence: Generated from business-rules.json rule BR-680
Tags: document management, data, document, file, template, management, downloadfile, documents, must, created, stored, updated, through

### EBR-0086

Downloadfile file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-740
Evidence: Generated from business-rules.json rule BR-740
Tags: document management, technical, document, file, template, management, downloadfile, movement, must, controlled, import, export, upload

### EBR-0087

Enquiryfile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-682
Evidence: Generated from business-rules.json rule BR-682
Tags: document management, data, document, file, template, management, enquiryfile, documents, must, created, stored, updated, through

### EBR-0088

Enquiryfile file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-741
Evidence: Generated from business-rules.json rule BR-741
Tags: document management, technical, document, file, template, management, enquiryfile, movement, must, controlled, import, export, upload

### EBR-0089

Enquiryfile records must follow the applicable opportunity lifecycle.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-683
Evidence: Generated from business-rules.json rule BR-683
Tags: document management, workflow, document, file, template, management, enquiryfile, records, must, follow, applicable, opportunity, lifecycle

### EBR-0090

Filecomment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-684
Evidence: Generated from business-rules.json rule BR-684
Tags: document management, data, document, file, template, management, filecomment, documents, must, created, stored, updated, through

### EBR-0091

Filecontent documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-685
Evidence: Generated from business-rules.json rule BR-685
Tags: document management, data, document, file, template, management, filecontent, documents, must, created, stored, updated, through

### EBR-0092

Filesharing documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-686
Evidence: Generated from business-rules.json rule BR-686
Tags: document management, data, document, file, template, management, filesharing, documents, must, created, stored, updated, through

### EBR-0093

Fileurl documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-687
Evidence: Generated from business-rules.json rule BR-687
Tags: document management, data, document, file, template, management, fileurl, documents, must, created, stored, updated, through

### EBR-0094

Fileversion documents must be created, stored, or updated through controlled document processes.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-688
Evidence: Generated from business-rules.json rule BR-688
Tags: audit, data, document, file, template, management, fileversion, documents, must, created, stored, updated, through

### EBR-0095

Formtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-689
Evidence: Generated from business-rules.json rule BR-689
Tags: document management, data, document, file, template, management, formtemplate, documents, must, created, stored, updated, through

### EBR-0096

Formtemplatedetail documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-690
Evidence: Generated from business-rules.json rule BR-690
Tags: document management, data, document, file, template, management, formtemplatedetail, documents, must, created, stored, updated, through

### EBR-0097

Formtemplatefieldlink documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-691
Evidence: Generated from business-rules.json rule BR-691
Tags: document management, data, document, file, template, management, formtemplatefieldlink, documents, must, created, stored, updated, through

### EBR-0098

Formtemplatefilecontent documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-692
Evidence: Generated from business-rules.json rule BR-692
Tags: document management, data, document, file, template, management, formtemplatefilecontent, documents, must, created, stored, updated, through

### EBR-0099

Formtemplatelookup documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-693
Evidence: Generated from business-rules.json rule BR-693
Tags: document management, data, document, file, template, management, formtemplatelookup, documents, must, created, stored, updated, through

### EBR-0100

Formtemplatetype documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-694
Evidence: Generated from business-rules.json rule BR-694
Tags: document management, data, document, file, template, management, formtemplatetype, documents, must, created, stored, updated, through

### EBR-0101

Getuploadurl documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-695
Evidence: Generated from business-rules.json rule BR-695
Tags: document management, data, document, file, template, management, getuploadurl, documents, must, created, stored, updated, through

### EBR-0102

Getuploadurl file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-742
Evidence: Generated from business-rules.json rule BR-742
Tags: document management, technical, document, file, template, management, getuploadurl, movement, must, controlled, import, export, upload

### EBR-0103

Milestones and stage gates must be completed before the next project phase starts.

Classification: Scheduling
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-656, BR-657, BR-658, BR-659, BR-660, BR-661, BR-662, BR-663, BR-667, BR-668, BR-669, BR-670, BR-671, BR-672, BR-673, BR-676, BR-677, BR-689, BR-690, BR-691, BR-692, BR-693, BR-694, BR-695, BR-696, BR-702, BR-703, BR-712, BR-713, BR-717, BR-718, BR-719, BR-720, BR-721, BR-722, BR-723, BR-724, BR-725, BR-726, BR-733, BR-734, BR-735, BR-736, BR-737, BR-742, BR-751, BR-752, BR-755, BR-756, BR-757, BR-758, BR-759
Evidence: Feature: Addstagegate Management; APIs: POST /add-stagegate/:templateId; Feature: Nonemptystagegate Management; APIs: GET /non-empty-stagegate/:templateId
Tags: scheduling, stagegate

### EBR-0104

Outcome documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-698
Evidence: Generated from business-rules.json rule BR-698
Tags: document management, data, document, file, template, management, outcome, documents, must, created, stored, updated, through

### EBR-0105

Pmwebform documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-699
Evidence: Generated from business-rules.json rule BR-699
Tags: document management, data, document, file, template, management, pmwebform, documents, must, created, stored, updated, through

### EBR-0106

Ptcfile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-701
Evidence: Generated from business-rules.json rule BR-701
Tags: document management, data, document, file, template, management, ptcfile, documents, must, created, stored, updated, through

### EBR-0107

Ptcfile file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-743
Evidence: Generated from business-rules.json rule BR-743
Tags: document management, technical, document, file, template, management, ptcfile, movement, must, controlled, import, export, upload

### EBR-0108

Publishedformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-702
Evidence: Generated from business-rules.json rule BR-702
Tags: document management, data, document, file, template, management, publishedformtemplate, documents, must, created, stored, updated, through

### EBR-0109

Publishformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-703
Evidence: Generated from business-rules.json rule BR-703
Tags: document management, data, document, file, template, management, publishformtemplate, documents, must, created, stored, updated, through

### EBR-0110

Referencefile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-705
Evidence: Generated from business-rules.json rule BR-705
Tags: document management, data, document, file, template, management, referencefile, documents, must, created, stored, updated, through

### EBR-0111

Referencefileurl documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-706
Evidence: Generated from business-rules.json rule BR-706
Tags: document management, data, document, file, template, management, referencefileurl, documents, must, created, stored, updated, through

### EBR-0112

Removeattachment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-708
Evidence: Generated from business-rules.json rule BR-708
Tags: document management, data, document, file, template, management, removeattachment, documents, must, created, stored, updated, through

### EBR-0113

Removefile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-711
Evidence: Generated from business-rules.json rule BR-711
Tags: document management, data, document, file, template, management, removefile, documents, must, created, stored, updated, through

### EBR-0114

Removetemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-713
Evidence: Generated from business-rules.json rule BR-713
Tags: document management, data, document, file, template, management, removetemplate, documents, must, created, stored, updated, through

### EBR-0115

Requestreferenceuploadurl documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-714
Evidence: Generated from business-rules.json rule BR-714
Tags: document management, data, document, file, template, management, requestreferenceuploadurl, documents, must, created, stored, updated, through

### EBR-0116

Requestreferenceuploadurl file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-744
Evidence: Generated from business-rules.json rule BR-744
Tags: document management, technical, document, file, template, management, requestreferenceuploadurl, movement, must, controlled, import, export, upload

### EBR-0117

Requestuploadurl documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-715
Evidence: Generated from business-rules.json rule BR-715
Tags: document management, data, document, file, template, management, requestuploadurl, documents, must, created, stored, updated, through

### EBR-0118

Requestuploadurl file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-745
Evidence: Generated from business-rules.json rule BR-745
Tags: document management, technical, document, file, template, management, requestuploadurl, movement, must, controlled, import, export, upload

### EBR-0119

Respondattachmentcomment collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-739
Evidence: Generated from business-rules.json rule BR-739
Tags: notification, business, document, file, template, management, respondattachmentcomment, collaboration, must, keep, messages, notifications, linked

### EBR-0120

Respondattachmentcomment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-716
Evidence: Generated from business-rules.json rule BR-716
Tags: document management, data, document, file, template, management, respondattachmentcomment, documents, must, created, stored, updated, through

### EBR-0121

Saveformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-717
Evidence: Generated from business-rules.json rule BR-717
Tags: document management, data, document, file, template, management, saveformtemplate, documents, must, created, stored, updated, through

### EBR-0122

Template documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-718
Evidence: Generated from business-rules.json rule BR-718
Tags: document management, data, document, file, template, management, documents, must, created, stored, updated, through, controlled

### EBR-0123

Templatedelete documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-720
Evidence: Generated from business-rules.json rule BR-720
Tags: document management, data, document, file, template, management, templatedelete, documents, must, created, stored, updated, through

### EBR-0124

Templatedetail documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-721
Evidence: Generated from business-rules.json rule BR-721
Tags: document management, data, document, file, template, management, templatedetail, documents, must, created, stored, updated, through

### EBR-0125

Templateinfo documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-722
Evidence: Generated from business-rules.json rule BR-722
Tags: document management, data, document, file, template, management, templateinfo, documents, must, created, stored, updated, through

### EBR-0126

Templateresponse documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-723
Evidence: Generated from business-rules.json rule BR-723
Tags: document management, data, document, file, template, management, templateresponse, documents, must, created, stored, updated, through

### EBR-0127

Templateresponse lifecycle actions must be enforced through workflow endpoints.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.82
Source Rule IDs: BR-656
Evidence: Generated from business-rules.json rule BR-656
Tags: document management, workflow, document, file, template, management, templateresponse, lifecycle, actions, must, enforced, through, endpoints

### EBR-0128

The system must maintain blueprint Lookup records as source data for Blueprintlookup.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-792
Evidence: Generated from business-rules.json rule BR-792
Tags: document management, data, document, file, template, management, system, must, maintain, blueprint, lookup, records, source

### EBR-0129

The system must maintain Blueprint Template records as source data for Blueprinttemplate.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-793
Evidence: Generated from business-rules.json rule BR-793
Tags: document management, data, document, file, template, management, system, must, maintain, blueprint, records, source, blueprinttemplate

### EBR-0130

The system must maintain File Content records as source data for Filecontent.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-794
Evidence: Generated from business-rules.json rule BR-794
Tags: document management, data, document, file, template, management, system, must, maintain, content, records, source, filecontent

### EBR-0131

The system must maintain File Sharing records as source data for Filesharing.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-795
Evidence: Generated from business-rules.json rule BR-795
Tags: document management, data, document, file, template, management, system, must, maintain, sharing, records, source, filesharing

### EBR-0132

The system must maintain Folder Sharing records as source data for Foldersharing.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-796
Evidence: Generated from business-rules.json rule BR-796
Tags: document management, data, document, file, template, management, system, must, maintain, folder, sharing, records, source

### EBR-0133

The system must maintain Form Template Field Link records as source data for Formtemplatefieldlink.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-797
Evidence: Generated from business-rules.json rule BR-797
Tags: document management, data, document, file, template, management, system, must, maintain, form, field, link, records

### EBR-0134

The system must maintain Form Template File Content records as source data for Formtemplatefilecontent.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-798
Evidence: Generated from business-rules.json rule BR-798
Tags: document management, data, document, file, template, management, system, must, maintain, form, content, records, source

### EBR-0135

The system must maintain Form Template Lookup records as source data for Formtemplatelookup.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-799
Evidence: Generated from business-rules.json rule BR-799
Tags: document management, data, document, file, template, management, system, must, maintain, form, lookup, records, source

### EBR-0136

The system must maintain Form Template records as source data for Formtemplate.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-800
Evidence: Generated from business-rules.json rule BR-800
Tags: document management, data, document, file, template, management, system, must, maintain, form, records, source, formtemplate

### EBR-0137

The system must maintain PMWeb Form records as source data for Pmwebform.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-801
Evidence: Generated from business-rules.json rule BR-801
Tags: document management, data, document, file, template, management, system, must, maintain, pmweb, form, records, source

### EBR-0138

The system must maintain Process Files records as source data for Processfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-802
Evidence: Generated from business-rules.json rule BR-802
Tags: document management, data, document, file, template, management, system, must, maintain, process, files, records, source

### EBR-0139

The system must maintain Task Files records as source data for Taskfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-803
Evidence: Generated from business-rules.json rule BR-803
Tags: document management, data, document, file, template, management, system, must, maintain, task, files, records, source

### EBR-0140

The system must maintain Template records as source data for Template.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-804
Evidence: Generated from business-rules.json rule BR-804
Tags: document management, data, document, file, template, management, system, must, maintain, records, source

### EBR-0141

The system must maintain Vendor records as source data for Vendor.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-805
Evidence: Generated from business-rules.json rule BR-805
Tags: document management, data, document, file, template, management, system, must, maintain, vendor, records, source

### EBR-0142

Updateformtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-724
Evidence: Generated from business-rules.json rule BR-724
Tags: document management, data, document, file, template, management, updateformtemplate, documents, must, created, stored, updated, through

### EBR-0143

Updatetemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-725
Evidence: Generated from business-rules.json rule BR-725
Tags: document management, data, document, file, template, management, updatetemplate, documents, must, created, stored, updated, through

### EBR-0144

Updatetemplatecollapsedview documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-726
Evidence: Generated from business-rules.json rule BR-726
Tags: document management, data, document, file, template, management, updatetemplatecollapsedview, documents, must, created, stored, updated, through

### EBR-0145

Uploadattachment documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-727
Evidence: Generated from business-rules.json rule BR-727
Tags: document management, data, document, file, template, management, uploadattachment, documents, must, created, stored, updated, through

### EBR-0146

Uploadattachment file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-746
Evidence: Generated from business-rules.json rule BR-746
Tags: document management, technical, document, file, template, management, uploadattachment, movement, must, controlled, import, export, upload

### EBR-0147

Uploadfile documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-729
Evidence: Generated from business-rules.json rule BR-729
Tags: document management, data, document, file, template, management, uploadfile, documents, must, created, stored, updated, through

### EBR-0148

Uploadfile file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-748
Evidence: Generated from business-rules.json rule BR-748
Tags: document management, technical, document, file, template, management, uploadfile, movement, must, controlled, import, export, upload

### EBR-0149

Uploadurl documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-730
Evidence: Generated from business-rules.json rule BR-730
Tags: document management, data, document, file, template, management, uploadurl, documents, must, created, stored, updated, through

### EBR-0150

Uploadurl file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-749
Evidence: Generated from business-rules.json rule BR-749
Tags: document management, technical, document, file, template, management, uploadurl, movement, must, controlled, import, export, upload

### EBR-0151

Vendor documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-731
Evidence: Generated from business-rules.json rule BR-731
Tags: document management, data, document, file, template, management, vendor, documents, must, created, stored, updated, through

### EBR-0152

Vendor file movement must use controlled import, export, upload, or download actions.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-750
Evidence: Generated from business-rules.json rule BR-750
Tags: document management, technical, document, file, template, management, vendor, movement, must, controlled, import, export, upload

### EBR-0153

Version and revision changes must preserve audit history.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-674, BR-675, BR-680, BR-681, BR-682, BR-683, BR-684, BR-685, BR-686, BR-687, BR-688, BR-692, BR-695, BR-700, BR-701, BR-704, BR-705, BR-706, BR-710, BR-711, BR-729, BR-732, BR-740, BR-741, BR-742, BR-743, BR-744, BR-745, BR-746, BR-747, BR-748, BR-749, BR-750, BR-760, BR-761, BR-762, BR-763, BR-764, BR-767, BR-769, BR-770, BR-789, BR-794, BR-795, BR-798, BR-802, BR-803, BR-823, BR-824, BR-825
Evidence: Feature: Version Management; APIs: GET /versions/:fileId
Tags: audit, version

### EBR-0154

Version documents must be created, stored, or updated through controlled document processes.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-732
Evidence: Generated from business-rules.json rule BR-732
Tags: audit, data, document, file, template, management, version, documents, must, created, stored, updated, through

### EBR-0155

Document, File and Template records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-751, BR-752, BR-753, BR-754, BR-755, BR-756, BR-757, BR-758, BR-759, BR-760, BR-761, BR-762, BR-763, BR-764, BR-765, BR-767, BR-768, BR-769, BR-771, BR-772, BR-773, BR-774, BR-775, BR-776, BR-777, BR-778, BR-779, BR-780, BR-781, BR-783, BR-786, BR-787, BR-788, BR-789, BR-790, BR-791
Evidence: Consolidated 36 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0156

Document, File and Template records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-664, BR-674, BR-676, BR-681, BR-697, BR-700, BR-704, BR-707, BR-710, BR-712, BR-719
Evidence: Consolidated 11 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0157

Document, File and Template records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-766, BR-770, BR-782, BR-784, BR-785
Evidence: Consolidated 5 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0158

Document, File and Template records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-809, BR-810, BR-811, BR-812, BR-813, BR-814, BR-815, BR-816, BR-817, BR-818, BR-819, BR-820, BR-821, BR-822, BR-823, BR-824, BR-825, BR-826, BR-827, BR-828, BR-829, BR-830, BR-831, BR-832, BR-833, BR-834, BR-835, BR-836, BR-837, BR-838, BR-839, BR-840, BR-841, BR-842, BR-843, BR-844, BR-845
Evidence: Consolidated 37 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Evaluation and Scoring

### EBR-0159

Createraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-291
Evidence: Generated from business-rules.json rule BR-291
Tags: raci, workflow, evaluation, scoring, createraci, work, must, have, clear, ownership, before, progress

### EBR-0160

Deleteraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-292
Evidence: Generated from business-rules.json rule BR-292
Tags: raci, workflow, evaluation, scoring, deleteraci, work, must, have, clear, ownership, before, progress

### EBR-0161

Evaluatorsteptemplate records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-297
Evidence: Generated from business-rules.json rule BR-297
Tags: state transition, workflow, evaluation, scoring, evaluatorsteptemplate, records, must, move, through, defined, states

### EBR-0162

Only Accountable users may approve workflow items.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.9
Source Rule IDs: BR-291, BR-292, BR-293, BR-294, BR-295, BR-296, BR-298, BR-299, BR-300, BR-301, BR-302, BR-303, BR-304, BR-307, BR-316
Evidence: Feature: Createraci Management; APIs: POST /create-raci; Feature: Deleteraci Management; APIs: POST /delete-raci; Feature: Processraci Management; Collections: ProcessRaci; Feature: Raci Management; APIs: GET /raci; Collections: Raci; Feature: Removeprocessraci Management; APIs: DELETE /remove-process-raci
Tags: raci, approval, accountable

### EBR-0163

Processraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-293
Evidence: Generated from business-rules.json rule BR-293
Tags: raci, workflow, evaluation, scoring, processraci, work, must, have, clear, ownership, before, progress

### EBR-0164

Raci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-294
Evidence: Generated from business-rules.json rule BR-294
Tags: raci, workflow, evaluation, scoring, work, must, have, clear, ownership, before, progress

### EBR-0165

Removeprocessraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-295
Evidence: Generated from business-rules.json rule BR-295
Tags: raci, workflow, evaluation, scoring, removeprocessraci, work, must, have, clear, ownership, before, progress

### EBR-0166

The system must maintain Process Raci records as source data for Processraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-304
Evidence: Generated from business-rules.json rule BR-304
Tags: raci, data, evaluation, scoring, system, must, maintain, process, records, source, processraci

### EBR-0167

The system must maintain Raci records as source data for Raci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-307
Evidence: Generated from business-rules.json rule BR-307
Tags: raci, data, evaluation, scoring, system, must, maintain, records, source

### EBR-0168

The system must maintain PTC records as source data for Ptc.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-305
Evidence: Generated from business-rules.json rule BR-305
Tags: validation, data, evaluation, scoring, system, must, maintain, records, source

### EBR-0169

The system must maintain PTCCounter records as source data for Ptccounter.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-306
Evidence: Generated from business-rules.json rule BR-306
Tags: validation, data, evaluation, scoring, system, must, maintain, ptccounter, records, source

### EBR-0170

Evaluation and Scoring records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-298, BR-299, BR-300, BR-301, BR-302, BR-303
Evidence: Consolidated 6 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0171

Evaluation and Scoring records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-296
Evidence: Consolidated 1 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0172

Evaluation and Scoring records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-308, BR-309, BR-310, BR-311, BR-312, BR-313, BR-314, BR-315, BR-316
Evidence: Consolidated 9 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## General

### EBR-0173

The system must maintain Booking records as source data for Booking.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-989
Evidence: Generated from business-rules.json rule BR-989
Tags: validation, data, general, system, must, maintain, booking, records, source

### EBR-0174

The system must maintain DOALevel records as source data for Doalevel.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-990
Evidence: Generated from business-rules.json rule BR-990
Tags: validation, data, general, system, must, maintain, doalevel, records, source

### EBR-0175

The system must maintain Meeting records as source data for Meeting.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-991
Evidence: Generated from business-rules.json rule BR-991
Tags: validation, data, general, system, must, maintain, meeting, records, source

### EBR-0176

Users must select an existing Distribute record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-992
Evidence: Generated from business-rules.json rule BR-992
Tags: validation, data, general, users, must, select, existing, distribute, record, before, detail, actions, performed

### EBR-0177

Users must select an existing Link record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-993
Evidence: Generated from business-rules.json rule BR-993
Tags: validation, data, general, users, must, select, existing, link, record, before, detail, actions, performed

### EBR-0178

Users must select an existing Meetingminute record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-994
Evidence: Generated from business-rules.json rule BR-994
Tags: validation, data, general, users, must, select, existing, meetingminute, record, before, detail, actions, performed

### EBR-0179

General records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-971, BR-972, BR-973, BR-974, BR-975, BR-976, BR-977, BR-978, BR-980, BR-981, BR-982, BR-985, BR-986
Evidence: Consolidated 13 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0180

General records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-968, BR-969, BR-970
Evidence: Consolidated 3 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0181

General records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-979, BR-983, BR-984, BR-987, BR-988
Evidence: Consolidated 5 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0182

General records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-1000, BR-1001, BR-1002, BR-1003, BR-1004, BR-1005, BR-1006, BR-1007, BR-1008, BR-995, BR-996, BR-997, BR-998, BR-999
Evidence: Consolidated 14 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Identity and Access Management

### EBR-0183

Access to Getracirole must be governed by user roles and permissions.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.84
Source Rule IDs: BR-020
Evidence: Generated from business-rules.json rule BR-020
Tags: raci, authorization, identity, access, management, getracirole, must, governed, user, roles, permissions

### EBR-0184

Getracirole work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-049
Evidence: Generated from business-rules.json rule BR-049
Tags: raci, workflow, identity, access, management, getracirole, work, must, have, clear, ownership, before, progress

### EBR-0185

Managersubmit records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-060
Evidence: Generated from business-rules.json rule BR-060
Tags: state transition, workflow, identity, access, management, managersubmit, records, must, move, through, defined, states

### EBR-0186

Only Accountable users may approve workflow items.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.9
Source Rule IDs: BR-007, BR-008, BR-009, BR-010, BR-011, BR-012, BR-013, BR-014, BR-015, BR-016, BR-017, BR-018, BR-019, BR-020, BR-021, BR-022, BR-023, BR-024, BR-025, BR-026, BR-027, BR-028, BR-029, BR-030, BR-031, BR-032, BR-033, BR-034, BR-035, BR-036, BR-037, BR-038, BR-039, BR-040, BR-041, BR-042, BR-043, BR-044, BR-045, BR-049, BR-083, BR-094, BR-129, BR-130, BR-131, BR-132, BR-133, BR-134, BR-145, BR-158
Evidence: Feature: Getracirole Management; APIs: GET /get-raci-roles
Tags: raci, approval, accountable

### EBR-0187

Participant must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-001, BR-002, BR-003, BR-004, BR-005, BR-006, BR-007, BR-008, BR-009, BR-010, BR-011, BR-012, BR-013, BR-014, BR-015, BR-016, BR-017, BR-018, BR-019, BR-020, BR-021, BR-022, BR-023, BR-024, BR-025, BR-026, BR-027, BR-028, BR-029, BR-030, BR-031, BR-032, BR-033, BR-034, BR-035, BR-036, BR-037, BR-038, BR-039, BR-040, BR-041, BR-042, BR-043, BR-044, BR-045, BR-049, BR-052, BR-057, BR-061, BR-062
Evidence: Feature: Participant Management; APIs: DELETE /:id/participants/:userId, GET /:id/participants, POST /:id/participants, PUT /:id/participants/:userId, PUT /:id/participants/:userId/status
Tags: state transition, workflow, state-transition

### EBR-0188

Participant records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-061
Evidence: Generated from business-rules.json rule BR-061
Tags: state transition, workflow, identity, access, management, participant, records, must, move, through, defined, states

### EBR-0189

Participant status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-062
Evidence: Generated from business-rules.json rule BR-062
Tags: state transition, workflow, identity, access, management, participant, status, must, maintained, each, tracked, record

### EBR-0190

Authentication actions must authenticate users before access is granted.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.86
Source Rule IDs: BR-001
Evidence: Generated from business-rules.json rule BR-001
Tags: validation, authorization, identity, access, management, authentication, actions, must, authenticate, users, before, granted

### EBR-0191

Generateloginotp actions must authenticate users before access is granted.

Classification: Validation
Testing Value Score: 9
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-002
Evidence: Generated from business-rules.json rule BR-002
Tags: validation, authorization, identity, access, management, generateloginotp, actions, must, authenticate, users, before, granted

### EBR-0192

Onboardingmanager onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-046
Evidence: Generated from business-rules.json rule BR-046
Tags: validation, workflow, identity, access, management, onboardingmanager, onboarding, must, completed, before, active, vendor, participation

### EBR-0193

Passwordreset actions must authenticate users before access is granted.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.86
Source Rule IDs: BR-004
Evidence: Generated from business-rules.json rule BR-004
Tags: validation, authorization, identity, access, management, passwordreset, actions, must, authenticate, users, before, granted

### EBR-0194

Passwordresetrequest actions must authenticate users before access is granted.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.86
Source Rule IDs: BR-005
Evidence: Generated from business-rules.json rule BR-005
Tags: validation, authorization, identity, access, management, passwordresetrequest, actions, must, authenticate, users, before, granted

### EBR-0195

Users must be able to find Departmentlist records before selecting detail actions.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.62
Source Rule IDs: BR-157
Evidence: Generated from business-rules.json rule BR-157
Tags: validation, business, identity, access, management, users, must, able, find, departmentlist, records, before, selecting

### EBR-0196

Users must be able to find Getpmweblistvalue records before selecting detail actions.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.62
Source Rule IDs: BR-158
Evidence: Generated from business-rules.json rule BR-158
Tags: validation, business, identity, access, management, users, must, able, find, getpmweblistvalue, records, before, selecting

### EBR-0197

Users must be able to find List records before selecting detail actions.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.62
Source Rule IDs: BR-159
Evidence: Generated from business-rules.json rule BR-159
Tags: validation, business, identity, access, management, users, must, able, find, list, records, before, selecting

### EBR-0198

Users must be able to find Userdepartmentlist records before selecting detail actions.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.62
Source Rule IDs: BR-160
Evidence: Generated from business-rules.json rule BR-160
Tags: validation, business, identity, access, management, users, must, able, find, userdepartmentlist, records, before, selecting

### EBR-0199

Users must select an existing Participant record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-112
Evidence: Generated from business-rules.json rule BR-112
Tags: validation, data, identity, access, management, users, must, select, existing, participant, record, before, detail

### EBR-0200

Users must select an existing Topic record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-113
Evidence: Generated from business-rules.json rule BR-113
Tags: validation, data, identity, access, management, users, must, select, existing, topic, record, before, detail

### EBR-0201

Vendordepartmentdetail onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-047
Evidence: Generated from business-rules.json rule BR-047
Tags: validation, workflow, identity, access, management, vendordepartmentdetail, onboarding, must, completed, before, active, vendor, participation

### EBR-0202

Vendorlogin actions must authenticate users before access is granted.

Classification: Validation
Testing Value Score: 9
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-006
Evidence: Generated from business-rules.json rule BR-006
Tags: validation, authorization, identity, access, management, vendorlogin, actions, must, authenticate, users, before, granted

### EBR-0203

Vendorlogin onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: Critical
Confidence: 0.83
Source Rule IDs: BR-048
Evidence: Generated from business-rules.json rule BR-048
Tags: validation, workflow, identity, access, management, vendorlogin, onboarding, must, completed, before, active, vendor, participation

### EBR-0204

Access to Allocatedto must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-007
Evidence: Generated from business-rules.json rule BR-007
Tags: authorization, identity, access, management, allocatedto, must, governed, user, roles, permissions

### EBR-0205

Access to Alluser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-008
Evidence: Generated from business-rules.json rule BR-008
Tags: authorization, identity, access, management, alluser, must, governed, user, roles, permissions

### EBR-0206

Access to Createdby must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-009
Evidence: Generated from business-rules.json rule BR-009
Tags: authorization, identity, access, management, createdby, must, governed, user, roles, permissions

### EBR-0207

Access to Customfolder must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-010
Evidence: Generated from business-rules.json rule BR-010
Tags: authorization, identity, access, management, customfolder, must, governed, user, roles, permissions

### EBR-0208

Access to Deleterole must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-011
Evidence: Generated from business-rules.json rule BR-011
Tags: authorization, identity, access, management, deleterole, must, governed, user, roles, permissions

### EBR-0209

Access to Department must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-012
Evidence: Generated from business-rules.json rule BR-012
Tags: authorization, identity, access, management, department, must, governed, user, roles, permissions

### EBR-0210

Access to Departmentuser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-013
Evidence: Generated from business-rules.json rule BR-013
Tags: authorization, identity, access, management, departmentuser, must, governed, user, roles, permissions

### EBR-0211

Access to File must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-014
Evidence: Generated from business-rules.json rule BR-014
Tags: authorization, identity, access, management, file, must, governed, user, roles, permissions

### EBR-0212

Access to Fileaccessaudit must be governed by user roles and permissions.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-015
Evidence: Generated from business-rules.json rule BR-015
Tags: audit, authorization, identity, access, management, fileaccessaudit, must, governed, user, roles, permissions

### EBR-0213

Access to Folder must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-016
Evidence: Generated from business-rules.json rule BR-016
Tags: authorization, identity, access, management, folder, must, governed, user, roles, permissions

### EBR-0214

Access to Getcommunitydetailsuser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-017
Evidence: Generated from business-rules.json rule BR-017
Tags: authorization, identity, access, management, getcommunitydetailsuser, must, governed, user, roles, permissions

### EBR-0215

Access to Getdepartment must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-018
Evidence: Generated from business-rules.json rule BR-018
Tags: authorization, identity, access, management, getdepartment, must, governed, user, roles, permissions

### EBR-0216

Access to Getpmwebuser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-019
Evidence: Generated from business-rules.json rule BR-019
Tags: authorization, identity, access, management, getpmwebuser, must, governed, user, roles, permissions

### EBR-0217

Access to Getuserdoc must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-021
Evidence: Generated from business-rules.json rule BR-021
Tags: authorization, identity, access, management, getuserdoc, must, governed, user, roles, permissions

### EBR-0218

Access to Itemuser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-022
Evidence: Generated from business-rules.json rule BR-022
Tags: authorization, identity, access, management, itemuser, must, governed, user, roles, permissions

### EBR-0219

Access to Myitem must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-023
Evidence: Generated from business-rules.json rule BR-023
Tags: authorization, identity, access, management, myitem, must, governed, user, roles, permissions

### EBR-0220

Access to Notifyuser must be governed by user roles and permissions.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-024
Evidence: Generated from business-rules.json rule BR-024
Tags: notification, authorization, identity, access, management, notifyuser, must, governed, user, roles, permissions

### EBR-0221

Access to Participant must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-025
Evidence: Generated from business-rules.json rule BR-025
Tags: authorization, identity, access, management, participant, must, governed, user, roles, permissions

### EBR-0222

Access to Projectuser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-026
Evidence: Generated from business-rules.json rule BR-026
Tags: authorization, identity, access, management, projectuser, must, governed, user, roles, permissions

### EBR-0223

Access to Removeuser must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-027
Evidence: Generated from business-rules.json rule BR-027
Tags: authorization, identity, access, management, removeuser, must, governed, user, roles, permissions

### EBR-0224

Access to Roles Permissions must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-028
Evidence: Generated from business-rules.json rule BR-028
Tags: authorization, identity, access, management, roles, permissions, must, governed, user

### EBR-0225

Access to Topic must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-029
Evidence: Generated from business-rules.json rule BR-029
Tags: authorization, identity, access, management, topic, must, governed, user, roles, permissions

### EBR-0226

Access to User must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-030
Evidence: Generated from business-rules.json rule BR-030
Tags: authorization, identity, access, management, user, must, governed, roles, permissions

### EBR-0227

Access to Userallthread must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-031
Evidence: Generated from business-rules.json rule BR-031
Tags: authorization, identity, access, management, userallthread, must, governed, user, roles, permissions

### EBR-0228

Access to Usercommunityphaseasset must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-032
Evidence: Generated from business-rules.json rule BR-032
Tags: authorization, identity, access, management, usercommunityphaseasset, must, governed, user, roles, permissions

### EBR-0229

Access to Usercommunityphaseproject must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-033
Evidence: Generated from business-rules.json rule BR-033
Tags: authorization, identity, access, management, usercommunityphaseproject, must, governed, user, roles, permissions

### EBR-0230

Access to Userdepartmentlist must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-034
Evidence: Generated from business-rules.json rule BR-034
Tags: authorization, identity, access, management, userdepartmentlist, must, governed, user, roles, permissions

### EBR-0231

Access to Usergroup must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-035
Evidence: Generated from business-rules.json rule BR-035
Tags: authorization, identity, access, management, usergroup, must, governed, user, roles, permissions

### EBR-0232

Access to Useritemthread must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-036
Evidence: Generated from business-rules.json rule BR-036
Tags: authorization, identity, access, management, useritemthread, must, governed, user, roles, permissions

### EBR-0233

Access to Userlinkagelog must be governed by user roles and permissions.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-037
Evidence: Generated from business-rules.json rule BR-037
Tags: audit, authorization, identity, access, management, userlinkagelog, must, governed, user, roles, permissions

### EBR-0234

Access to Userlist must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-038
Evidence: Generated from business-rules.json rule BR-038
Tags: authorization, identity, access, management, userlist, must, governed, user, roles, permissions

### EBR-0235

Access to Usermapping must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-039
Evidence: Generated from business-rules.json rule BR-039
Tags: authorization, identity, access, management, usermapping, must, governed, user, roles, permissions

### EBR-0236

Access to Usernotification must be governed by user roles and permissions.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-040
Evidence: Generated from business-rules.json rule BR-040
Tags: notification, authorization, identity, access, management, usernotification, must, governed, user, roles, permissions

### EBR-0237

Access to Useropportunitythread must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-041
Evidence: Generated from business-rules.json rule BR-041
Tags: authorization, identity, access, management, useropportunitythread, must, governed, user, roles, permissions

### EBR-0238

Access to Userproject must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-042
Evidence: Generated from business-rules.json rule BR-042
Tags: authorization, identity, access, management, userproject, must, governed, user, roles, permissions

### EBR-0239

Access to Userreplacement must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-043
Evidence: Generated from business-rules.json rule BR-043
Tags: authorization, identity, access, management, userreplacement, must, governed, user, roles, permissions

### EBR-0240

Access to Userrole must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-044
Evidence: Generated from business-rules.json rule BR-044
Tags: authorization, identity, access, management, userrole, must, governed, user, roles, permissions

### EBR-0241

Access to Userstarreditem must be governed by user roles and permissions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-045
Evidence: Generated from business-rules.json rule BR-045
Tags: authorization, identity, access, management, userstarreditem, must, governed, user, roles, permissions

### EBR-0242

File documents must be created, stored, or updated through controlled document processes.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-054
Evidence: Generated from business-rules.json rule BR-054
Tags: authorization, data, identity, access, management, file, documents, must, created, stored, updated, through, controlled

### EBR-0243

Fileaccessaudit documents must be created, stored, or updated through controlled document processes.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-055
Evidence: Generated from business-rules.json rule BR-055
Tags: audit, authorization, identity, access, management, fileaccessaudit, documents, must, created, stored, updated, through, controlled

### EBR-0244

Functiondepartment changes must be managed through administrative controls.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.74
Source Rule IDs: BR-066
Evidence: Generated from business-rules.json rule BR-066
Tags: authorization, business, identity, access, management, functiondepartment, changes, must, managed, through, administrative, controls

### EBR-0245

Identity actions must enforce authentication and authorization controls.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.86
Source Rule IDs: BR-003
Evidence: Generated from business-rules.json rule BR-003
Tags: authorization, identity, access, management, actions, must, enforce, authentication, controls

### EBR-0246

Managersubmit lifecycle actions must be enforced through workflow endpoints.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.82
Source Rule IDs: BR-050
Evidence: Generated from business-rules.json rule BR-050
Tags: authorization, workflow, identity, access, management, managersubmit, lifecycle, actions, must, enforced, through, endpoints

### EBR-0247

Notifications must be generated on workflow state changes.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.82
Source Rule IDs: BR-001, BR-002, BR-004, BR-005, BR-006, BR-007, BR-008, BR-009, BR-010, BR-011, BR-012, BR-013, BR-014, BR-015, BR-016, BR-017, BR-018, BR-019, BR-020, BR-021, BR-022, BR-023, BR-024, BR-025, BR-026, BR-027, BR-028, BR-029, BR-030, BR-031, BR-032, BR-033, BR-034, BR-035, BR-036, BR-037, BR-038, BR-039, BR-040, BR-041, BR-042, BR-043, BR-044, BR-045, BR-063, BR-067, BR-069, BR-083, BR-086, BR-093
Evidence: Feature: Notifyuser Management; APIs: POST /notify-user; Feature: Usernotification Management; Collections: UserNotification
Tags: notification, workflow

### EBR-0248

Registerreferenceupload documents must be created, stored, or updated through controlled document processes.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-058
Evidence: Generated from business-rules.json rule BR-058
Tags: authorization, data, identity, access, management, registerreferenceupload, documents, must, created, stored, updated, through, controlled

### EBR-0249

Registerreferenceupload file movement must use controlled import, export, upload, or download actions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-064
Evidence: Generated from business-rules.json rule BR-064
Tags: authorization, technical, identity, access, management, registerreferenceupload, file, movement, must, controlled, import, export, upload

### EBR-0250

Registerupload documents must be created, stored, or updated through controlled document processes.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-059
Evidence: Generated from business-rules.json rule BR-059
Tags: authorization, data, identity, access, management, registerupload, documents, must, created, stored, updated, through, controlled

### EBR-0251

Registerupload file movement must use controlled import, export, upload, or download actions.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.76
Source Rule IDs: BR-065
Evidence: Generated from business-rules.json rule BR-065
Tags: authorization, technical, identity, access, management, registerupload, file, movement, must, controlled, import, export, upload

### EBR-0252

The system must maintain Company Department records as source data for Companydepartment.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-096
Evidence: Generated from business-rules.json rule BR-096
Tags: authorization, data, identity, access, management, system, must, maintain, company, department, records, source, companydepartment

### EBR-0253

The system must maintain Department records as source data for Department.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-097
Evidence: Generated from business-rules.json rule BR-097
Tags: authorization, data, identity, access, management, system, must, maintain, department, records, source

### EBR-0254

The system must maintain Department Type records as source data for Departmenttype.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-098
Evidence: Generated from business-rules.json rule BR-098
Tags: authorization, data, identity, access, management, system, must, maintain, department, type, records, source, departmenttype

### EBR-0255

The system must maintain PMWeb List records as source data for Pmweblist.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-099
Evidence: Generated from business-rules.json rule BR-099
Tags: authorization, data, identity, access, management, system, must, maintain, pmweb, list, records, source, pmweblist

### EBR-0256

The system must maintain PMWeb List Value records as source data for Pmweblistvalue.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-100
Evidence: Generated from business-rules.json rule BR-100
Tags: authorization, data, identity, access, management, system, must, maintain, pmweb, list, value, records, source

### EBR-0257

The system must maintain Project Users records as source data for Projectuser.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-101
Evidence: Generated from business-rules.json rule BR-101
Tags: authorization, data, identity, access, management, system, must, maintain, project, users, records, source, projectuser

### EBR-0258

The system must maintain Topic records as source data for Topic.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-102
Evidence: Generated from business-rules.json rule BR-102
Tags: authorization, data, identity, access, management, system, must, maintain, topic, records, source

### EBR-0259

The system must maintain User Group records as source data for Usergroup.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-103
Evidence: Generated from business-rules.json rule BR-103
Tags: authorization, data, identity, access, management, system, must, maintain, user, group, records, source, usergroup

### EBR-0260

The system must maintain User List records as source data for Userlist.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-104
Evidence: Generated from business-rules.json rule BR-104
Tags: authorization, data, identity, access, management, system, must, maintain, user, list, records, source, userlist

### EBR-0261

The system must maintain User Mapping records as source data for Usermapping.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-105
Evidence: Generated from business-rules.json rule BR-105
Tags: authorization, data, identity, access, management, system, must, maintain, user, mapping, records, source, usermapping

### EBR-0262

The system must maintain User Notification records as source data for Usernotification.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-106
Evidence: Generated from business-rules.json rule BR-106
Tags: notification, data, identity, access, management, system, must, maintain, user, records, source, usernotification

### EBR-0263

The system must maintain User records as source data for User.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-107
Evidence: Generated from business-rules.json rule BR-107
Tags: authorization, data, identity, access, management, system, must, maintain, user, records, source

### EBR-0264

The system must maintain User Replacement records as source data for Userreplacement.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-108
Evidence: Generated from business-rules.json rule BR-108
Tags: authorization, data, identity, access, management, system, must, maintain, user, replacement, records, source, userreplacement

### EBR-0265

The system must maintain User Role records as source data for Userrole.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-109
Evidence: Generated from business-rules.json rule BR-109
Tags: authorization, data, identity, access, management, system, must, maintain, user, role, records, source, userrole

### EBR-0266

The system must maintain User Starred Item records as source data for Userstarreditem.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-110
Evidence: Generated from business-rules.json rule BR-110
Tags: authorization, data, identity, access, management, system, must, maintain, user, starred, item, records, source

### EBR-0267

The system must maintain Vendor Department Detail records as source data for Vendordepartmentdetail.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-111
Evidence: Generated from business-rules.json rule BR-111
Tags: authorization, data, identity, access, management, system, must, maintain, vendor, department, detail, records, source

### EBR-0268

Usermapping changes must be managed through administrative controls.

Classification: Authorization
Testing Value Score: 8
Business Criticality: High
Confidence: 0.74
Source Rule IDs: BR-067
Evidence: Generated from business-rules.json rule BR-067
Tags: authorization, business, identity, access, management, usermapping, changes, must, managed, through, administrative, controls

### EBR-0269

Usernotification collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-063
Evidence: Generated from business-rules.json rule BR-063
Tags: notification, business, identity, access, management, usernotification, collaboration, must, keep, messages, notifications, linked, related

### EBR-0270

Identity and Access records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-068, BR-069, BR-070, BR-071, BR-072, BR-073, BR-075, BR-076, BR-077, BR-079, BR-080, BR-081, BR-082, BR-083, BR-084, BR-085, BR-086, BR-087, BR-089, BR-090, BR-091, BR-092, BR-093, BR-094, BR-095
Evidence: Consolidated 25 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0271

Identity and Access records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-051, BR-052, BR-053, BR-056, BR-057
Evidence: Consolidated 5 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0272

Identity and Access records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-074, BR-078, BR-088
Evidence: Consolidated 3 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0273

Identity and Access records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-114, BR-115, BR-116, BR-117, BR-118, BR-119, BR-120, BR-121, BR-122, BR-123, BR-124, BR-125, BR-126, BR-127, BR-128, BR-129, BR-130, BR-131, BR-132, BR-133, BR-134, BR-135, BR-136, BR-137, BR-138, BR-139, BR-140, BR-141, BR-142, BR-143, BR-144, BR-145, BR-146, BR-147, BR-148, BR-149, BR-150, BR-151, BR-152, BR-153, BR-154, BR-155, BR-156
Evidence: Consolidated 43 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Location and Asset Management

### EBR-0274

Only Accountable users may approve workflow items.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.9
Source Rule IDs: BR-955, BR-962, BR-963, BR-967
Evidence: Feature: Raciallocation Management; APIs: GET /raci-allocations; Collections: RaciAllocation
Tags: raci, approval, accountable

### EBR-0275

Raciallocation work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-955
Evidence: Generated from business-rules.json rule BR-955
Tags: raci, workflow, location, asset, management, raciallocation, work, must, have, clear, ownership, before, progress

### EBR-0276

The system must maintain Raci Allocation records as source data for Raciallocation.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-962
Evidence: Generated from business-rules.json rule BR-962
Tags: raci, data, location, asset, management, system, must, maintain, allocation, records, source, raciallocation

### EBR-0277

The system must maintain Asset Class records as source data for Assetclass.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-958
Evidence: Generated from business-rules.json rule BR-958
Tags: validation, data, location, asset, management, system, must, maintain, class, records, source, assetclass

### EBR-0278

The system must maintain Asset records as source data for Asset.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-959
Evidence: Generated from business-rules.json rule BR-959
Tags: validation, data, location, asset, management, system, must, maintain, records, source

### EBR-0279

The system must maintain Country records as source data for Country.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-961
Evidence: Generated from business-rules.json rule BR-961
Tags: validation, data, location, asset, management, system, must, maintain, country, records, source

### EBR-0280

The system must maintain Asset Typology records as source data for Assettypology.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-960
Evidence: Generated from business-rules.json rule BR-960
Tags: audit, data, location, asset, management, system, must, maintain, typology, records, source, assettypology

### EBR-0281

Location and Asset records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-956, BR-957
Evidence: Consolidated 2 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0282

Location and Asset records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-963, BR-964, BR-965, BR-966, BR-967
Evidence: Consolidated 5 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Opportunity and Procurement Lifecycle

### EBR-0283

Addrfpstep records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-165
Evidence: Generated from business-rules.json rule BR-165
Tags: workflow, opportunity, procurement, lifecycle, addrfpstep, records, must, follow, applicable

### EBR-0284

Addrfpstep records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-198
Evidence: Generated from business-rules.json rule BR-198
Tags: state transition, workflow, opportunity, procurement, lifecycle, addrfpstep, records, must, move, through, defined, states

### EBR-0285

Awardcompany records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-166
Evidence: Generated from business-rules.json rule BR-166
Tags: workflow, opportunity, procurement, lifecycle, awardcompany, records, must, follow, applicable

### EBR-0286

Completeeoi lifecycle actions must be enforced through workflow endpoints.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-163
Evidence: Generated from business-rules.json rule BR-163
Tags: workflow, opportunity, procurement, lifecycle, completeeoi, actions, must, enforced, through, endpoints

### EBR-0287

Completeeoi records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-167
Evidence: Generated from business-rules.json rule BR-167
Tags: workflow, opportunity, procurement, lifecycle, completeeoi, records, must, follow, applicable

### EBR-0288

Completeeoi records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-199
Evidence: Generated from business-rules.json rule BR-199
Tags: state transition, workflow, opportunity, procurement, lifecycle, completeeoi, records, must, move, through, defined, states

### EBR-0289

Completerfp lifecycle actions must be enforced through workflow endpoints.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-164
Evidence: Generated from business-rules.json rule BR-164
Tags: workflow, opportunity, procurement, lifecycle, completerfp, actions, must, enforced, through, endpoints

### EBR-0290

Completerfp records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-168
Evidence: Generated from business-rules.json rule BR-168
Tags: workflow, opportunity, procurement, lifecycle, completerfp, records, must, follow, applicable

### EBR-0291

Completerfp records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-200
Evidence: Generated from business-rules.json rule BR-200
Tags: state transition, workflow, opportunity, procurement, lifecycle, completerfp, records, must, move, through, defined, states

### EBR-0292

Editeoi records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-169
Evidence: Generated from business-rules.json rule BR-169
Tags: workflow, opportunity, procurement, lifecycle, editeoi, records, must, follow, applicable

### EBR-0293

Editrfp records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-170
Evidence: Generated from business-rules.json rule BR-170
Tags: workflow, opportunity, procurement, lifecycle, editrfp, records, must, follow, applicable

### EBR-0294

Enquiry records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-171
Evidence: Generated from business-rules.json rule BR-171
Tags: workflow, opportunity, procurement, lifecycle, enquiry, records, must, follow, applicable

### EBR-0295

Enquirycounter records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-172
Evidence: Generated from business-rules.json rule BR-172
Tags: workflow, opportunity, procurement, lifecycle, enquirycounter, records, must, follow, applicable

### EBR-0296

Eoi records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-173
Evidence: Generated from business-rules.json rule BR-173
Tags: workflow, opportunity, procurement, lifecycle, records, must, follow, applicable

### EBR-0297

Eoidetail records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-174
Evidence: Generated from business-rules.json rule BR-174
Tags: workflow, opportunity, procurement, lifecycle, eoidetail, records, must, follow, applicable

### EBR-0298

General must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-171, BR-172, BR-174, BR-175, BR-176, BR-180, BR-201, BR-202, BR-215, BR-216, BR-226, BR-227, BR-229, BR-239, BR-243, BR-244
Evidence: Feature: General; APIs: DELETE /, DELETE /:enquiryId, DELETE /:id, DELETE /:ptcId, GET /, GET /:id, GET /:itemId, GET /status
Tags: state transition, workflow, state-transition

### EBR-0299

General records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-176
Evidence: Generated from business-rules.json rule BR-176
Tags: workflow, opportunity, procurement, lifecycle, general, records, must, follow, applicable

### EBR-0300

General records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-201
Evidence: Generated from business-rules.json rule BR-201
Tags: state transition, workflow, opportunity, procurement, lifecycle, general, records, must, move, through, defined, states

### EBR-0301

General status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-202
Evidence: Generated from business-rules.json rule BR-202
Tags: state transition, workflow, opportunity, procurement, lifecycle, general, status, must, maintained, each, tracked, record

### EBR-0302

Opportunity records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-178
Evidence: Generated from business-rules.json rule BR-178
Tags: workflow, opportunity, procurement, lifecycle, records, must, follow, applicable

### EBR-0303

Opportunityaward records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-179
Evidence: Generated from business-rules.json rule BR-179
Tags: workflow, opportunity, procurement, lifecycle, opportunityaward, records, must, follow, applicable

### EBR-0304

Opportunitybidopening records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-180
Evidence: Generated from business-rules.json rule BR-180
Tags: workflow, opportunity, procurement, lifecycle, opportunitybidopening, records, must, follow, applicable

### EBR-0305

Opportunityblueprint records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-181
Evidence: Generated from business-rules.json rule BR-181
Tags: workflow, opportunity, procurement, lifecycle, opportunityblueprint, records, must, follow, applicable

### EBR-0306

Opportunitycustomfolder records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-182
Evidence: Generated from business-rules.json rule BR-182
Tags: workflow, opportunity, procurement, lifecycle, opportunitycustomfolder, records, must, follow, applicable

### EBR-0307

Opportunityelementthread records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-184
Evidence: Generated from business-rules.json rule BR-184
Tags: workflow, opportunity, procurement, lifecycle, opportunityelementthread, records, must, follow, applicable

### EBR-0308

Opportunityevaluation records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-185
Evidence: Generated from business-rules.json rule BR-185
Tags: workflow, opportunity, procurement, lifecycle, opportunityevaluation, records, must, follow, applicable

### EBR-0309

Opportunityexecution records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-186
Evidence: Generated from business-rules.json rule BR-186
Tags: workflow, opportunity, procurement, lifecycle, opportunityexecution, records, must, follow, applicable

### EBR-0310

Opportunityexecution records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-203
Evidence: Generated from business-rules.json rule BR-203
Tags: state transition, workflow, opportunity, procurement, lifecycle, opportunityexecution, records, must, move, through, defined, states

### EBR-0311

Opportunityexecutionblock records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-187
Evidence: Generated from business-rules.json rule BR-187
Tags: workflow, opportunity, procurement, lifecycle, opportunityexecutionblock, records, must, follow, applicable

### EBR-0312

Opportunityexecutionblock records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-204
Evidence: Generated from business-rules.json rule BR-204
Tags: state transition, workflow, opportunity, procurement, lifecycle, opportunityexecutionblock, records, must, move, through, defined, states

### EBR-0313

Opportunityexecutionvendorblock records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-188
Evidence: Generated from business-rules.json rule BR-188
Tags: workflow, opportunity, procurement, lifecycle, opportunityexecutionvendorblock, records, must, follow, applicable

### EBR-0314

Opportunityexecutionvendorblock records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-205
Evidence: Generated from business-rules.json rule BR-205
Tags: state transition, workflow, opportunity, procurement, lifecycle, opportunityexecutionvendorblock, records, must, move, through, defined, states

### EBR-0315

Opportunitystructure records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-191
Evidence: Generated from business-rules.json rule BR-191
Tags: workflow, opportunity, procurement, lifecycle, opportunitystructure, records, must, follow, applicable

### EBR-0316

Opportunitythread records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-192
Evidence: Generated from business-rules.json rule BR-192
Tags: workflow, opportunity, procurement, lifecycle, opportunitythread, records, must, follow, applicable

### EBR-0317

Removerfpstep records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-193
Evidence: Generated from business-rules.json rule BR-193
Tags: workflow, opportunity, procurement, lifecycle, removerfpstep, records, must, follow, applicable

### EBR-0318

Removerfpstep records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-206
Evidence: Generated from business-rules.json rule BR-206
Tags: state transition, workflow, opportunity, procurement, lifecycle, removerfpstep, records, must, move, through, defined, states

### EBR-0319

Rfp records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-194
Evidence: Generated from business-rules.json rule BR-194
Tags: workflow, opportunity, procurement, lifecycle, records, must, follow, applicable

### EBR-0320

Rfpdetail records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-195
Evidence: Generated from business-rules.json rule BR-195
Tags: workflow, opportunity, procurement, lifecycle, rfpdetail, records, must, follow, applicable

### EBR-0321

Upserteoi records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-196
Evidence: Generated from business-rules.json rule BR-196
Tags: workflow, opportunity, procurement, lifecycle, upserteoi, records, must, follow, applicable

### EBR-0322

Upsertrfp records must follow the applicable opportunity lifecycle.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-197
Evidence: Generated from business-rules.json rule BR-197
Tags: workflow, opportunity, procurement, lifecycle, upsertrfp, records, must, follow, applicable

### EBR-0323

Opportunity onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-161
Evidence: Generated from business-rules.json rule BR-161
Tags: validation, workflow, opportunity, procurement, lifecycle, onboarding, must, completed, before, active, vendor, participation

### EBR-0324

Opportunityexecutionvendorblock onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-162
Evidence: Generated from business-rules.json rule BR-162
Tags: validation, workflow, opportunity, procurement, lifecycle, opportunityexecutionvendorblock, onboarding, must, completed, before, active, vendor, participation

### EBR-0325

The system must maintain Enquiry Counter records as source data for Enquirycounter.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-226
Evidence: Generated from business-rules.json rule BR-226
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, enquiry, counter, records, source, enquirycounter

### EBR-0326

The system must maintain enquiry records as source data for Enquiry.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-227
Evidence: Generated from business-rules.json rule BR-227
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, enquiry, records, source

### EBR-0327

The system must maintain Opportunity Award records as source data for Opportunityaward.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-228
Evidence: Generated from business-rules.json rule BR-228
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, award, records, source, opportunityaward

### EBR-0328

The system must maintain Opportunity Bid Opening records as source data for Opportunitybidopening.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-229
Evidence: Generated from business-rules.json rule BR-229
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, opening, records, source, opportunitybidopening

### EBR-0329

The system must maintain Opportunity Custom Folder records as source data for Opportunitycustomfolder.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-230
Evidence: Generated from business-rules.json rule BR-230
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, custom, folder, records, source, opportunitycustomfolder

### EBR-0330

The system must maintain Opportunity Evaluation records as source data for Opportunityevaluation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-232
Evidence: Generated from business-rules.json rule BR-232
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, evaluation, records, source, opportunityevaluation

### EBR-0331

The system must maintain Opportunity Execution Block records as source data for Opportunityexecutionblock.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-233
Evidence: Generated from business-rules.json rule BR-233
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, execution, block, records, source, opportunityexecutionblock

### EBR-0332

The system must maintain Opportunity Execution records as source data for Opportunityexecution.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-234
Evidence: Generated from business-rules.json rule BR-234
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, execution, records, source, opportunityexecution

### EBR-0333

The system must maintain Opportunity Execution Vendor Block records as source data for Opportunityexecutionvendorblock.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-235
Evidence: Generated from business-rules.json rule BR-235
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, execution, vendor, block, records, source

### EBR-0334

The system must maintain Opportunity records as source data for Opportunity.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-236
Evidence: Generated from business-rules.json rule BR-236
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, records, source

### EBR-0335

The system must maintain Opportunity Thread records as source data for Opportunitythread.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-238
Evidence: Generated from business-rules.json rule BR-238
Tags: validation, data, opportunity, procurement, lifecycle, system, must, maintain, thread, records, source, opportunitythread

### EBR-0336

Users must select an existing General record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-239
Evidence: Generated from business-rules.json rule BR-239
Tags: validation, data, opportunity, procurement, lifecycle, users, must, select, existing, general, record, before, detail

### EBR-0337

Collaboration threads must preserve comments and attachments with the related business record.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.78
Source Rule IDs: BR-161, BR-162, BR-165, BR-166, BR-167, BR-168, BR-169, BR-170, BR-171, BR-172, BR-173, BR-174, BR-176, BR-177, BR-178, BR-179, BR-180, BR-181, BR-182, BR-183, BR-184, BR-185, BR-186, BR-187, BR-188, BR-189, BR-190, BR-191, BR-192, BR-193, BR-194, BR-195, BR-196, BR-197, BR-203, BR-204, BR-205, BR-207, BR-208, BR-218, BR-219, BR-220, BR-228, BR-229, BR-230, BR-231, BR-232, BR-233, BR-234, BR-235
Evidence: Feature: Opportunitythread Management; Collections: OpportunityThread
Tags: audit, collaboration

### EBR-0338

Opportunityreferenceattachmentaudit documents must be created, stored, or updated through controlled document processes.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-189
Evidence: Generated from business-rules.json rule BR-189
Tags: audit, data, opportunity, procurement, lifecycle, opportunityreferenceattachmentaudit, documents, must, created, stored, updated, through, controlled

### EBR-0339

Opportunityreferenceattachmentaudit records must follow the applicable opportunity lifecycle.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-190
Evidence: Generated from business-rules.json rule BR-190
Tags: audit, workflow, opportunity, procurement, lifecycle, opportunityreferenceattachmentaudit, records, must, follow, applicable

### EBR-0340

Opportunitythread collaboration must keep messages and notifications linked to the related business record.

Classification: Notification
Testing Value Score: 8
Business Criticality: High
Confidence: 0.77
Source Rule IDs: BR-207
Evidence: Generated from business-rules.json rule BR-207
Tags: notification, business, opportunity, procurement, lifecycle, opportunitythread, collaboration, must, keep, messages, notifications, linked, related

### EBR-0341

The system must maintain Opportunity Reference Attachment Audit records as source data for Opportunityreferenceattachmentaudit.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-237
Evidence: Generated from business-rules.json rule BR-237
Tags: audit, data, opportunity, procurement, lifecycle, system, must, maintain, reference, attachment, records, source

### EBR-0342

Version and revision changes must preserve audit history.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-161, BR-162, BR-165, BR-166, BR-167, BR-168, BR-169, BR-170, BR-171, BR-172, BR-173, BR-174, BR-176, BR-177, BR-178, BR-179, BR-180, BR-181, BR-182, BR-183, BR-184, BR-185, BR-186, BR-187, BR-188, BR-189, BR-190, BR-191, BR-192, BR-193, BR-194, BR-195, BR-196, BR-197, BR-203, BR-204, BR-205, BR-207, BR-208, BR-209, BR-210, BR-211, BR-212, BR-213, BR-214, BR-215, BR-217, BR-218, BR-219, BR-220
Evidence: Feature: Opportunity Management; APIs: DELETE /opportunity/delete, GET /opportunity/details, GET /opportunity/log, GET /opportunity/revisions, GET /opportunity/vendor-log, POST /opportunity/create, POST /opportunity/members, POST /opportunity/new-revision; Collections: Opportunity
Tags: audit, version

### EBR-0343

Opportunitydefinition changes must be managed through administrative controls.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.74
Source Rule IDs: BR-208
Evidence: Generated from business-rules.json rule BR-208
Tags: configuration, business, opportunity, procurement, lifecycle, opportunitydefinition, changes, must, managed, through, administrative, controls

### EBR-0344

Opportunitydefinition records must follow the applicable opportunity lifecycle.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-183
Evidence: Generated from business-rules.json rule BR-183
Tags: configuration, workflow, opportunity, procurement, lifecycle, opportunitydefinition, records, must, follow, applicable

### EBR-0345

The system must maintain Opportunity Definition records as source data for Opportunitydefinition.

Classification: Configuration
Testing Value Score: 6
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-231
Evidence: Generated from business-rules.json rule BR-231
Tags: configuration, data, opportunity, procurement, lifecycle, system, must, maintain, definition, records, source, opportunitydefinition

### EBR-0346

Opportunity and Procurement lifecycle records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-209, BR-210, BR-211, BR-212, BR-213, BR-214, BR-215, BR-217, BR-218, BR-219, BR-220, BR-221, BR-222, BR-223, BR-224, BR-225
Evidence: Consolidated 16 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0347

Opportunity and Procurement lifecycle records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-175, BR-177
Evidence: Consolidated 2 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0348

Opportunity and Procurement lifecycle records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-216
Evidence: Consolidated 1 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0349

Opportunity and Procurement lifecycle records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-240, BR-241, BR-242, BR-243, BR-244, BR-245, BR-246, BR-247, BR-248, BR-249, BR-250, BR-251
Evidence: Consolidated 12 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Project and Activity Management

### EBR-0350

Activity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-323, BR-324, BR-325, BR-326, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-342, BR-343, BR-345, BR-346, BR-348, BR-349, BR-350, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-372, BR-374, BR-376, BR-380, BR-381, BR-383, BR-385, BR-386, BR-388, BR-389, BR-391, BR-392
Evidence: Feature: Activity Management; APIs: GET /activities/:taskId; Collections: Activity
Tags: state transition, workflow, state-transition

### EBR-0351

Activitychecklist must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-364, BR-365, BR-366, BR-367, BR-371, BR-372, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423
Evidence: Feature: Activitychecklist Management; Collections: ActivityChecklist
Tags: state transition, workflow, state-transition

### EBR-0352

Activitychecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-352
Evidence: Generated from business-rules.json rule BR-352
Tags: state transition, workflow, project, activity, management, activitychecklist, records, must, move, through, defined, states

### EBR-0353

Activityfile must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423, BR-428, BR-429, BR-430, BR-431, BR-437, BR-442
Evidence: Feature: Activityfile Management; Collections: ActivityFiles
Tags: state transition, workflow, state-transition

### EBR-0354

Activityraci must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-343, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-399, BR-401, BR-404, BR-406, BR-410
Evidence: Feature: Activityraci Management; Collections: ActivityRaci
Tags: state transition, workflow, state-transition

### EBR-0355

Activityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-317
Evidence: Generated from business-rules.json rule BR-317
Tags: raci, workflow, project, activity, management, activityraci, work, must, have, clear, ownership, before, progress

### EBR-0356

Activityrelationship must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423, BR-428, BR-429, BR-430, BR-431, BR-442, BR-443
Evidence: Feature: Activityrelationship Management; APIs: GET /activity-relationship
Tags: state transition, workflow, state-transition

### EBR-0357

Addactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-323, BR-324, BR-325, BR-326, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-342, BR-343, BR-345, BR-346, BR-348, BR-349, BR-350, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-372, BR-374, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-383, BR-385, BR-386, BR-388
Evidence: Feature: Addactivity Management; APIs: POST /add-activity/:taskId
Tags: state transition, workflow, state-transition

### EBR-0358

Addprocess must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-319, BR-320, BR-322, BR-333, BR-335, BR-337, BR-338, BR-339, BR-341, BR-343, BR-344, BR-346, BR-347, BR-349, BR-351, BR-359, BR-360, BR-361, BR-362, BR-363, BR-374, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-384, BR-389, BR-390, BR-391, BR-392, BR-394, BR-395, BR-398, BR-399, BR-400, BR-405, BR-409, BR-413, BR-427, BR-436, BR-437, BR-438, BR-439, BR-441, BR-450, BR-462, BR-466, BR-467
Evidence: Feature: Addprocess Management; APIs: POST /add-process/:stagegateId
Tags: state transition, workflow, state-transition

### EBR-0359

Addsubactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-343, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-374, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-383, BR-385, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-396, BR-399, BR-401, BR-404, BR-406, BR-409
Evidence: Feature: Addsubactivity Management; APIs: POST /add-subactivity/:activityId
Tags: state transition, workflow, state-transition

### EBR-0360

Checklistprojectsource records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-353
Evidence: Generated from business-rules.json rule BR-353
Tags: state transition, workflow, project, activity, management, checklistprojectsource, records, must, move, through, defined, states

### EBR-0361

Copyactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-384, BR-385, BR-386, BR-388, BR-389, BR-391, BR-393, BR-394, BR-395, BR-396, BR-397, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423, BR-428
Evidence: Feature: Copyactivity Management; APIs: POST /copy-activity
Tags: state transition, workflow, state-transition

### EBR-0362

Copystagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-335, BR-347, BR-362, BR-363, BR-379, BR-383, BR-384, BR-385, BR-386, BR-393, BR-394, BR-395, BR-396, BR-397, BR-400, BR-413, BR-441, BR-450, BR-462, BR-466, BR-467, BR-477
Evidence: Feature: Copystagegate Management; APIs: POST /copy-stagegate
Tags: state transition, workflow, state-transition

### EBR-0363

Deleteprojectstagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-347, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-378, BR-379, BR-382, BR-384, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-394
Evidence: Feature: Deleteprojectstagegate Management; APIs: DELETE /delete-project-stagegate
Tags: state transition, workflow, state-transition

### EBR-0364

Getprojectstagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-346, BR-347, BR-349, BR-351, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-374, BR-378, BR-379, BR-382, BR-384, BR-388, BR-389, BR-390
Evidence: Feature: Getprojectstagegate Management; APIs: GET /get-project-stagegate/:stagegateId
Tags: state transition, workflow, state-transition

### EBR-0365

Only Accountable users may approve workflow items.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.9
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-372, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-382, BR-383, BR-385, BR-386, BR-388, BR-389, BR-391, BR-392, BR-393, BR-396, BR-397, BR-399, BR-400, BR-401, BR-402, BR-404, BR-406, BR-407, BR-410, BR-413, BR-414, BR-415, BR-419, BR-430, BR-438, BR-441, BR-442, BR-443, BR-444, BR-445, BR-446, BR-447, BR-448, BR-449, BR-453, BR-455, BR-456, BR-457, BR-459, BR-462, BR-466, BR-472, BR-476
Evidence: Feature: Activityraci Management; Collections: ActivityRaci; Feature: Projectactivityraci Management; Collections: ProjectActivityRaci; Feature: Projectprocessraci Management; Collections: ProjectProcessRaci; Feature: Projectracidetail Management; APIs: POST /project-raci-detail; Feature: Projectremoveactivityraci Management; APIs: DELETE /project-remove-activity-raci; Feature: Projectremoveprocessraci Management; APIs: DELETE /project-remove-process-raci; Feature: Projectremovesubactivityraci Management; APIs: DELETE /project-remove-subactivity-raci; Feature: Projectremovetaskraci Management; APIs: DELETE /project-remove-task-raci; Feature: Projectsubactivityraci Management; Collections: ProjectSubActivityRaci; Feature: Projecttaskraci Management; Collections: ProjectTaskRaci; Feature: Raciallocationsproject Management; APIs: GET /raci-allocations-projects; Feature: Removeactivityraci Management; APIs: DELETE /remove-activity-raci; Feature: Removesubactivityraci Management; APIs: DELETE /remove-subactivity-raci; Feature: Removetaskraci Management; APIs: DELETE /remove-task-raci; Feature: Subactivityraci Management; Collections: SubActivityRaci; Feature: Taskraci Management; Collections: TaskRaci
Tags: raci, approval, accountable

### EBR-0366

Primaveraactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423, BR-424, BR-425, BR-426, BR-428, BR-429, BR-430
Evidence: Feature: Primaveraactivity Management; APIs: GET /primavera-activities; Collections: PrimaveraActivity
Tags: state transition, workflow, state-transition

### EBR-0367

Process must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-319, BR-320, BR-322, BR-333, BR-335, BR-337, BR-338, BR-339, BR-341, BR-343, BR-344, BR-346, BR-347, BR-349, BR-351, BR-359, BR-360, BR-361, BR-362, BR-363, BR-374, BR-377, BR-379, BR-384, BR-390, BR-394, BR-395, BR-398, BR-399, BR-400, BR-405, BR-409, BR-413, BR-427, BR-436, BR-437, BR-438, BR-439, BR-441, BR-450, BR-462, BR-466, BR-467, BR-476, BR-477, BR-482, BR-486, BR-489
Evidence: Feature: Process Management; APIs: GET /processes/:stagegateId; Collections: Process
Tags: state transition, workflow, state-transition

### EBR-0368

Projectactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-350, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367
Evidence: Feature: Projectactivity Management; APIs: GET /project-activities/:taskId; Collections: ProjectActivity
Tags: state transition, workflow, state-transition

### EBR-0369

Projectactivitychecklist must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-372
Evidence: Feature: Projectactivitychecklist Management; Collections: ProjectActivityChecklist
Tags: state transition, workflow, state-transition

### EBR-0370

Projectactivitychecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-354
Evidence: Generated from business-rules.json rule BR-354
Tags: state transition, workflow, project, activity, management, projectactivitychecklist, records, must, move, through, defined, states

### EBR-0371

Projectactivityfile must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-376
Evidence: Feature: Projectactivityfile Management; Collections: ProjectActivityFiles
Tags: state transition, workflow, state-transition

### EBR-0372

Projectactivityraci must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368
Evidence: Feature: Projectactivityraci Management; Collections: ProjectActivityRaci
Tags: state transition, workflow, state-transition

### EBR-0373

Projectactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-318
Evidence: Generated from business-rules.json rule BR-318
Tags: raci, workflow, project, activity, management, projectactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0374

Projectactivitystatu must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-376
Evidence: Feature: Projectactivitystatu Management; APIs: POST /project-activity-status
Tags: state transition, workflow, state-transition

### EBR-0375

Projectactivitystatu records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-355
Evidence: Generated from business-rules.json rule BR-355
Tags: state transition, workflow, project, activity, management, projectactivitystatu, records, must, move, through, defined, states

### EBR-0376

Projectactivitystatu status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-356
Evidence: Generated from business-rules.json rule BR-356
Tags: state transition, workflow, project, activity, management, projectactivitystatu, status, must, maintained, each, tracked, record

### EBR-0377

Projectaddactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-350, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367
Evidence: Feature: Projectaddactivity Management; APIs: POST /project-add-activity/:taskId
Tags: state transition, workflow, state-transition

### EBR-0378

Projectaddprocess must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-346, BR-347, BR-349, BR-351, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-374, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381
Evidence: Feature: Projectaddprocess Management; APIs: POST /project-add-process/:stagegateId
Tags: state transition, workflow, state-transition

### EBR-0379

Projectaddsubactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371
Evidence: Feature: Projectaddsubactivity Management; APIs: POST /project-add-subactivity/:activityId
Tags: state transition, workflow, state-transition

### EBR-0380

Projectchecklistclosureattachment records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-357
Evidence: Generated from business-rules.json rule BR-357
Tags: state transition, workflow, project, activity, management, projectchecklistclosureattachment, records, must, move, through, defined, states

### EBR-0381

Projectchecklistlink records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-358
Evidence: Generated from business-rules.json rule BR-358
Tags: state transition, workflow, project, activity, management, projectchecklistlink, records, must, move, through, defined, states

### EBR-0382

Projectcopyactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-376
Evidence: Feature: Projectcopyactivity Management; APIs: POST /project-copy-activity
Tags: state transition, workflow, state-transition

### EBR-0383

Projectcopystagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-347, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-378, BR-379, BR-382, BR-383, BR-384, BR-385, BR-386, BR-388, BR-389, BR-390, BR-391
Evidence: Feature: Projectcopystagegate Management; APIs: POST /project-copy-stagegate
Tags: state transition, workflow, state-transition

### EBR-0384

Projectprocess must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-346, BR-347, BR-349, BR-351, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-374, BR-377, BR-378, BR-379, BR-382, BR-384, BR-388
Evidence: Feature: Projectprocess Management; APIs: GET /project-processes/:stagegateId; Collections: ProjectProcess
Tags: state transition, workflow, state-transition

### EBR-0385

Projectprocesschecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-359
Evidence: Generated from business-rules.json rule BR-359
Tags: state transition, workflow, project, activity, management, projectprocesschecklist, records, must, move, through, defined, states

### EBR-0386

Projectprocessraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-319
Evidence: Generated from business-rules.json rule BR-319
Tags: raci, workflow, project, activity, management, projectprocessraci, work, must, have, clear, ownership, before, progress

### EBR-0387

Projectprocessstatu must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-347, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-377, BR-378, BR-379, BR-382, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393
Evidence: Feature: Projectprocessstatu Management; APIs: POST /project-process-status
Tags: state transition, workflow, state-transition

### EBR-0388

Projectprocessstatu records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-360
Evidence: Generated from business-rules.json rule BR-360
Tags: state transition, workflow, project, activity, management, projectprocessstatu, records, must, move, through, defined, states

### EBR-0389

Projectprocessstatu status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-361
Evidence: Generated from business-rules.json rule BR-361
Tags: state transition, workflow, project, activity, management, projectprocessstatu, status, must, maintained, each, tracked, record

### EBR-0390

Projectracidetail work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-320
Evidence: Generated from business-rules.json rule BR-320
Tags: raci, workflow, project, activity, management, projectracidetail, work, must, have, clear, ownership, before, progress

### EBR-0391

Projectremoveactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367
Evidence: Feature: Projectremoveactivity Management; APIs: DELETE /project-remove-activity
Tags: state transition, workflow, state-transition

### EBR-0392

Projectremoveactivityraci must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366
Evidence: Feature: Projectremoveactivityraci Management; APIs: DELETE /project-remove-activity-raci
Tags: state transition, workflow, state-transition

### EBR-0393

Projectremoveactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-321
Evidence: Generated from business-rules.json rule BR-321
Tags: raci, workflow, project, activity, management, projectremoveactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0394

Projectremoveprocessraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-322
Evidence: Generated from business-rules.json rule BR-322
Tags: raci, workflow, project, activity, management, projectremoveprocessraci, work, must, have, clear, ownership, before, progress

### EBR-0395

Projectremovesubactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-323
Evidence: Generated from business-rules.json rule BR-323
Tags: raci, workflow, project, activity, management, projectremovesubactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0396

Projectremovetaskraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-324
Evidence: Generated from business-rules.json rule BR-324
Tags: raci, workflow, project, activity, management, projectremovetaskraci, work, must, have, clear, ownership, before, progress

### EBR-0397

Projectstagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-347, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-378, BR-379, BR-382, BR-384, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-394
Evidence: Feature: Projectstagegate Management; Collections: ProjectStagegate
Tags: state transition, workflow, state-transition

### EBR-0398

Projectstagegatestatu must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-347, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-378, BR-379, BR-382, BR-384, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-394
Evidence: Feature: Projectstagegatestatu Management; APIs: POST /project-stagegate-status
Tags: state transition, workflow, state-transition

### EBR-0399

Projectstagegatestatu records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-362
Evidence: Generated from business-rules.json rule BR-362
Tags: state transition, workflow, project, activity, management, projectstagegatestatu, records, must, move, through, defined, states

### EBR-0400

Projectstagegatestatu status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-363
Evidence: Generated from business-rules.json rule BR-363
Tags: state transition, workflow, project, activity, management, projectstagegatestatu, status, must, maintained, each, tracked, record

### EBR-0401

Projectsubactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371
Evidence: Feature: Projectsubactivity Management; APIs: GET /project-subactivities/:activityId; Collections: ProjectSubActivity
Tags: state transition, workflow, state-transition

### EBR-0402

Projectsubactivitychecklist must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-372
Evidence: Feature: Projectsubactivitychecklist Management; Collections: ProjectSubActivityChecklist
Tags: state transition, workflow, state-transition

### EBR-0403

Projectsubactivitychecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-364
Evidence: Generated from business-rules.json rule BR-364
Tags: state transition, workflow, project, activity, management, projectsubactivitychecklist, records, must, move, through, defined, states

### EBR-0404

Projectsubactivityfile must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-376
Evidence: Feature: Projectsubactivityfile Management; Collections: ProjectSubActivityFiles
Tags: state transition, workflow, state-transition

### EBR-0405

Projectsubactivityraci must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368
Evidence: Feature: Projectsubactivityraci Management; Collections: ProjectSubActivityRaci
Tags: state transition, workflow, state-transition

### EBR-0406

Projectsubactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-325
Evidence: Generated from business-rules.json rule BR-325
Tags: raci, workflow, project, activity, management, projectsubactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0407

Projectsubactivitystatu must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-329, BR-331, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-348, BR-349, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-378, BR-379, BR-380, BR-382, BR-385, BR-388, BR-389
Evidence: Feature: Projectsubactivitystatu Management; APIs: POST /project-subactivity-status
Tags: state transition, workflow, state-transition

### EBR-0408

Projectsubactivitystatu records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-365
Evidence: Generated from business-rules.json rule BR-365
Tags: state transition, workflow, project, activity, management, projectsubactivitystatu, records, must, move, through, defined, states

### EBR-0409

Projectsubactivitystatu status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-366
Evidence: Generated from business-rules.json rule BR-366
Tags: state transition, workflow, project, activity, management, projectsubactivitystatu, status, must, maintained, each, tracked, record

### EBR-0410

Projecttaskchecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-367
Evidence: Generated from business-rules.json rule BR-367
Tags: state transition, workflow, project, activity, management, projecttaskchecklist, records, must, move, through, defined, states

### EBR-0411

Projecttaskraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-326
Evidence: Generated from business-rules.json rule BR-326
Tags: raci, workflow, project, activity, management, projecttaskraci, work, must, have, clear, ownership, before, progress

### EBR-0412

Projecttaskstatu must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-330, BR-332, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-350, BR-351, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-372, BR-378, BR-379, BR-381, BR-382, BR-386, BR-388, BR-389
Evidence: Feature: Projecttaskstatu Management; APIs: POST /project-task-status
Tags: state transition, workflow, state-transition

### EBR-0413

Projecttaskstatu records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-368
Evidence: Generated from business-rules.json rule BR-368
Tags: state transition, workflow, project, activity, management, projecttaskstatu, records, must, move, through, defined, states

### EBR-0414

Projecttaskstatu status must be maintained for each tracked record.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-369
Evidence: Generated from business-rules.json rule BR-369
Tags: state transition, workflow, project, activity, management, projecttaskstatu, status, must, maintained, each, tracked, record

### EBR-0415

Projectupdateactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371
Evidence: Feature: Projectupdateactivity Management; APIs: PUT /project-update-activity/:activityId
Tags: state transition, workflow, state-transition

### EBR-0416

Projectupdatesubactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371
Evidence: Feature: Projectupdatesubactivity Management; APIs: PUT /project-update-subactivity/:subActivityId
Tags: state transition, workflow, state-transition

### EBR-0417

Raciallocationsproject work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-327
Evidence: Generated from business-rules.json rule BR-327
Tags: raci, workflow, project, activity, management, raciallocationsproject, work, must, have, clear, ownership, before, progress

### EBR-0418

Removeactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-328, BR-329, BR-330, BR-331, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-374, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-399, BR-401
Evidence: Feature: Removeactivity Management; APIs: DELETE /remove-activity/:activityId
Tags: state transition, workflow, state-transition

### EBR-0419

Removeactivityraci must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393
Evidence: Feature: Removeactivityraci Management; APIs: DELETE /remove-activity-raci
Tags: state transition, workflow, state-transition

### EBR-0420

Removeactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-328
Evidence: Generated from business-rules.json rule BR-328
Tags: raci, workflow, project, activity, management, removeactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0421

Removeprocessesfromstagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-320, BR-321, BR-322, BR-323, BR-324, BR-328, BR-329, BR-330, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-362, BR-363, BR-374, BR-379, BR-384, BR-395, BR-399, BR-400, BR-409, BR-413, BR-441, BR-450, BR-462, BR-466, BR-467, BR-477
Evidence: Feature: Removeprocessesfromstagegate Management; APIs: DELETE /remove-processes-from-stagegate/:stagegateId
Tags: state transition, workflow, state-transition

### EBR-0422

Removesubactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-329
Evidence: Generated from business-rules.json rule BR-329
Tags: raci, workflow, project, activity, management, removesubactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0423

Removetaskraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-330
Evidence: Generated from business-rules.json rule BR-330
Tags: raci, workflow, project, activity, management, removetaskraci, work, must, have, clear, ownership, before, progress

### EBR-0424

Stagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-335, BR-347, BR-362, BR-363, BR-379, BR-384, BR-395, BR-400, BR-413, BR-441, BR-450, BR-462, BR-466, BR-467, BR-477
Evidence: Feature: Stagegate Management; Collections: Stagegate
Tags: state transition, workflow, state-transition

### EBR-0425

Stageoption must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-335, BR-347, BR-362, BR-363, BR-370, BR-379, BR-384, BR-395, BR-400, BR-413, BR-441, BR-450, BR-462, BR-466, BR-467, BR-476, BR-477, BR-493
Evidence: Feature: Stageoption Management; APIs: GET /stage-options
Tags: state transition, workflow, state-transition

### EBR-0426

Stageoption records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-370
Evidence: Generated from business-rules.json rule BR-370
Tags: state transition, workflow, project, activity, management, stageoption, records, must, move, through, defined, states

### EBR-0427

Subactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-343, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-374, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-399, BR-401, BR-404, BR-406, BR-409, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420
Evidence: Feature: Subactivity Management; APIs: GET /subactivities/:activityId; Collections: SubActivity
Tags: state transition, workflow, state-transition

### EBR-0428

Subactivitychecklist must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-364, BR-365, BR-366, BR-367, BR-371, BR-372, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423
Evidence: Feature: Subactivitychecklist Management; Collections: SubActivityChecklist
Tags: state transition, workflow, state-transition

### EBR-0429

Subactivitychecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-371
Evidence: Generated from business-rules.json rule BR-371
Tags: state transition, workflow, project, activity, management, subactivitychecklist, records, must, move, through, defined, states

### EBR-0430

Subactivityfile must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-340, BR-341, BR-345, BR-346, BR-348, BR-349, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-401, BR-404, BR-406, BR-410, BR-414, BR-417, BR-418, BR-419, BR-420, BR-423, BR-428, BR-429, BR-430, BR-431, BR-437, BR-442
Evidence: Feature: Subactivityfile Management; Collections: SubActivityFiles
Tags: state transition, workflow, state-transition

### EBR-0431

Subactivityraci must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-343, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-399, BR-401, BR-404, BR-406, BR-410
Evidence: Feature: Subactivityraci Management; Collections: SubActivityRaci
Tags: state transition, workflow, state-transition

### EBR-0432

Subactivityraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-331
Evidence: Generated from business-rules.json rule BR-331
Tags: raci, workflow, project, activity, management, subactivityraci, work, must, have, clear, ownership, before, progress

### EBR-0433

Taskchecklist records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-372
Evidence: Generated from business-rules.json rule BR-372
Tags: state transition, workflow, project, activity, management, taskchecklist, records, must, move, through, defined, states

### EBR-0434

Taskraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-332
Evidence: Generated from business-rules.json rule BR-332
Tags: raci, workflow, project, activity, management, taskraci, work, must, have, clear, ownership, before, progress

### EBR-0435

The system must maintain Activity Checklist records as source data for Activitychecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-417
Evidence: Generated from business-rules.json rule BR-417
Tags: workflow, data, project, activity, management, system, must, maintain, checklist, records, source, activitychecklist

### EBR-0436

The system must maintain Activity Raci records as source data for Activityraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-419
Evidence: Generated from business-rules.json rule BR-419
Tags: raci, data, project, activity, management, system, must, maintain, records, source, activityraci

### EBR-0437

The system must maintain Activity records as source data for Activity.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-420
Evidence: Generated from business-rules.json rule BR-420
Tags: workflow, data, project, activity, management, system, must, maintain, records, source

### EBR-0438

The system must maintain Phase records as source data for Phase.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-421
Evidence: Generated from business-rules.json rule BR-421
Tags: workflow, data, project, activity, management, system, must, maintain, phase, records, source

### EBR-0439

The system must maintain Process records as source data for Process.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-427
Evidence: Generated from business-rules.json rule BR-427
Tags: workflow, data, project, activity, management, system, must, maintain, process, records, source

### EBR-0440

The system must maintain Project Activity Checklist records as source data for Projectactivitychecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-428
Evidence: Generated from business-rules.json rule BR-428
Tags: workflow, data, project, activity, management, system, must, maintain, checklist, records, source, projectactivitychecklist

### EBR-0441

The system must maintain Project Activity Raci records as source data for Projectactivityraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-430
Evidence: Generated from business-rules.json rule BR-430
Tags: raci, data, project, activity, management, system, must, maintain, records, source, projectactivityraci

### EBR-0442

The system must maintain Project Activity records as source data for Projectactivity.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-431
Evidence: Generated from business-rules.json rule BR-431
Tags: workflow, data, project, activity, management, system, must, maintain, records, source, projectactivity

### EBR-0443

The system must maintain Project Check List Closure Comments records as source data for Projectchecklistclosurecomment.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-432
Evidence: Generated from business-rules.json rule BR-432
Tags: state transition, data, project, activity, management, system, must, maintain, check, list, closure, comments, records

### EBR-0444

The system must maintain Project Checklist Closure Attachments records as source data for Projectchecklistclosureattachment.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-433
Evidence: Generated from business-rules.json rule BR-433
Tags: state transition, data, project, activity, management, system, must, maintain, checklist, closure, attachments, records, source

### EBR-0445

The system must maintain Project Checklist Links records as source data for Projectchecklistlink.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-434
Evidence: Generated from business-rules.json rule BR-434
Tags: workflow, data, project, activity, management, system, must, maintain, checklist, links, records, source, projectchecklistlink

### EBR-0446

The system must maintain Project Phase Asset Details records as source data for Projectphaseassetdetail.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-435
Evidence: Generated from business-rules.json rule BR-435
Tags: workflow, data, project, activity, management, system, must, maintain, phase, asset, details, records, source

### EBR-0447

The system must maintain Project Process Checklist records as source data for Projectprocesschecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-436
Evidence: Generated from business-rules.json rule BR-436
Tags: workflow, data, project, activity, management, system, must, maintain, process, checklist, records, source, projectprocesschecklist

### EBR-0448

The system must maintain Project Process Raci records as source data for Projectprocessraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-438
Evidence: Generated from business-rules.json rule BR-438
Tags: raci, data, project, activity, management, system, must, maintain, process, records, source, projectprocessraci

### EBR-0449

The system must maintain Project Process records as source data for Projectprocess.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-439
Evidence: Generated from business-rules.json rule BR-439
Tags: workflow, data, project, activity, management, system, must, maintain, process, records, source, projectprocess

### EBR-0450

The system must maintain Project records as source data for Project.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-440
Evidence: Generated from business-rules.json rule BR-440
Tags: workflow, data, project, activity, management, system, must, maintain, records, source

### EBR-0451

The system must maintain Project Stagegate records as source data for Projectstagegate.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-441
Evidence: Generated from business-rules.json rule BR-441
Tags: state transition, data, project, activity, management, system, must, maintain, stagegate, records, source, projectstagegate

### EBR-0452

The system must maintain Project Sub Activity Checklist records as source data for Projectsubactivitychecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-442
Evidence: Generated from business-rules.json rule BR-442
Tags: workflow, data, project, activity, management, system, must, maintain, checklist, records, source, projectsubactivitychecklist

### EBR-0453

The system must maintain Project Sub Activity Raci records as source data for Projectsubactivityraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-444
Evidence: Generated from business-rules.json rule BR-444
Tags: raci, data, project, activity, management, system, must, maintain, records, source, projectsubactivityraci

### EBR-0454

The system must maintain Project Sub Activity records as source data for Projectsubactivity.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-445
Evidence: Generated from business-rules.json rule BR-445
Tags: workflow, data, project, activity, management, system, must, maintain, records, source, projectsubactivity

### EBR-0455

The system must maintain Project Task Checklist records as source data for Projecttaskchecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-446
Evidence: Generated from business-rules.json rule BR-446
Tags: workflow, data, project, activity, management, system, must, maintain, task, checklist, records, source, projecttaskchecklist

### EBR-0456

The system must maintain Project Task Raci records as source data for Projecttaskraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-448
Evidence: Generated from business-rules.json rule BR-448
Tags: raci, data, project, activity, management, system, must, maintain, task, records, source, projecttaskraci

### EBR-0457

The system must maintain Project Task records as source data for Projecttask.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-449
Evidence: Generated from business-rules.json rule BR-449
Tags: workflow, data, project, activity, management, system, must, maintain, task, records, source, projecttask

### EBR-0458

The system must maintain Stagegate records as source data for Stagegate.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-450
Evidence: Generated from business-rules.json rule BR-450
Tags: state transition, data, project, activity, management, system, must, maintain, stagegate, records, source

### EBR-0459

The system must maintain Sub Activity Checklist records as source data for Subactivitychecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-451
Evidence: Generated from business-rules.json rule BR-451
Tags: workflow, data, project, activity, management, system, must, maintain, checklist, records, source, subactivitychecklist

### EBR-0460

The system must maintain Sub Activity Raci records as source data for Subactivityraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-453
Evidence: Generated from business-rules.json rule BR-453
Tags: raci, data, project, activity, management, system, must, maintain, records, source, subactivityraci

### EBR-0461

The system must maintain Sub Activity records as source data for Subactivity.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-454
Evidence: Generated from business-rules.json rule BR-454
Tags: workflow, data, project, activity, management, system, must, maintain, records, source, subactivity

### EBR-0462

The system must maintain Task Checklist records as source data for Taskchecklist.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-455
Evidence: Generated from business-rules.json rule BR-455
Tags: workflow, data, project, activity, management, system, must, maintain, task, checklist, records, source, taskchecklist

### EBR-0463

The system must maintain Task Raci records as source data for Taskraci.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-456
Evidence: Generated from business-rules.json rule BR-456
Tags: raci, data, project, activity, management, system, must, maintain, task, records, source, taskraci

### EBR-0464

The system must maintain Task records as source data for Task.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-457
Evidence: Generated from business-rules.json rule BR-457
Tags: workflow, data, project, activity, management, system, must, maintain, task, records, source

### EBR-0465

Timeline records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-373
Evidence: Generated from business-rules.json rule BR-373
Tags: state transition, workflow, project, activity, management, timeline, records, must, move, through, defined, states

### EBR-0466

Timelinevalidation records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-374
Evidence: Generated from business-rules.json rule BR-374
Tags: state transition, workflow, project, activity, management, timelinevalidation, records, must, move, through, defined, states

### EBR-0467

Updateactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-374, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-399, BR-401, BR-404, BR-405, BR-406, BR-407, BR-408, BR-409, BR-410, BR-411
Evidence: Feature: Updateactivity Management; APIs: PUT /update-activity/:activityId
Tags: state transition, workflow, state-transition

### EBR-0468

Updateprojectstagegate must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-347, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-378, BR-379, BR-382, BR-384, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393
Evidence: Feature: Updateprojectstagegate Management; APIs: POST /update-project-stagegate
Tags: state transition, workflow, state-transition

### EBR-0469

Updatesubactivity must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-317, BR-318, BR-320, BR-321, BR-323, BR-325, BR-328, BR-329, BR-331, BR-333, BR-336, BR-337, BR-339, BR-340, BR-341, BR-343, BR-344, BR-345, BR-346, BR-348, BR-349, BR-351, BR-352, BR-354, BR-355, BR-356, BR-364, BR-365, BR-366, BR-371, BR-374, BR-376, BR-380, BR-383, BR-385, BR-388, BR-389, BR-391, BR-393, BR-396, BR-399, BR-401, BR-404, BR-405, BR-406, BR-407, BR-408, BR-409, BR-410, BR-411
Evidence: Feature: Updatesubactivity Management; APIs: PUT /update-subactivity/:subActivityId
Tags: state transition, workflow, state-transition

### EBR-0470

Upserttimeline records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-375
Evidence: Generated from business-rules.json rule BR-375
Tags: state transition, workflow, project, activity, management, upserttimeline, records, must, move, through, defined, states

### EBR-0471

Mandatory checklist items must be completed before workflow progression.

Classification: Validation
Testing Value Score: 9
Business Criticality: Critical
Confidence: 0.88
Source Rule IDs: BR-317, BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-331, BR-332, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-352, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-371, BR-372, BR-374, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-382, BR-383, BR-385, BR-386, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-396, BR-397, BR-401, BR-402, BR-404, BR-406, BR-407, BR-410, BR-414, BR-415, BR-417, BR-418, BR-419, BR-420, BR-423, BR-428, BR-432, BR-433, BR-434, BR-436, BR-442, BR-446, BR-447, BR-448, BR-449, BR-451, BR-455, BR-456, BR-457, BR-459, BR-469, BR-472, BR-488, BR-491, BR-495
Evidence: Feature: Activitychecklist Management; Collections: ActivityChecklist; Feature: Checklistprojectsource Management; APIs: GET /checklist-project-sources/:projectId; Feature: Projectactivitychecklist Management; Collections: ProjectActivityChecklist; Feature: Projectchecklistclosureattachment Management; Collections: ProjectChecklistClosureAttachments; Feature: Projectchecklistlink Management; Collections: ProjectChecklistLinks; Feature: Projectprocesschecklist Management; Collections: ProjectProcessChecklist; Feature: Projectsubactivitychecklist Management; Collections: ProjectSubActivityChecklist; Feature: Projecttaskchecklist Management; Collections: ProjectTaskChecklist; Feature: Subactivitychecklist Management; Collections: SubActivityChecklist; Feature: Taskchecklist Management; Collections: TaskChecklist
Tags: validation, checklist, mandatory, workflow

### EBR-0472

Users must select an existing Reschedule record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-458
Evidence: Generated from business-rules.json rule BR-458
Tags: validation, data, project, activity, management, users, must, select, existing, reschedule, record, before, detail

### EBR-0473

Users must select an existing Task record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-459
Evidence: Generated from business-rules.json rule BR-459
Tags: validation, data, project, activity, management, users, must, select, existing, task, record, before, detail

### EBR-0474

Alltemplateactivity documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-333
Evidence: Generated from business-rules.json rule BR-333
Tags: document management, data, project, activity, management, alltemplateactivity, documents, must, created, stored, updated, through, controlled

### EBR-0475

Milestones and stage gates must be completed before the next project phase starts.

Classification: Scheduling
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-318, BR-319, BR-320, BR-321, BR-322, BR-323, BR-324, BR-325, BR-326, BR-327, BR-328, BR-329, BR-330, BR-333, BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-344, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351, BR-353, BR-354, BR-355, BR-356, BR-357, BR-358, BR-359, BR-360, BR-361, BR-362, BR-363, BR-364, BR-365, BR-366, BR-367, BR-368, BR-369, BR-373, BR-374, BR-375, BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-382, BR-383, BR-384, BR-385, BR-386, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-394, BR-395, BR-396, BR-397, BR-398, BR-399, BR-400, BR-405, BR-409, BR-413, BR-416, BR-427, BR-436, BR-437, BR-438, BR-439, BR-441, BR-450, BR-462, BR-466, BR-467, BR-476, BR-477, BR-482, BR-486, BR-489, BR-496
Evidence: Feature: Addprocess Management; APIs: POST /add-process/:stagegateId; Feature: Copystagegate Management; APIs: POST /copy-stagegate; Feature: Deleteprojectstagegate Management; APIs: DELETE /delete-project-stagegate; Feature: Getprojectstagegate Management; APIs: GET /get-project-stagegate/:stagegateId; Feature: Process Management; APIs: GET /processes/:stagegateId; Collections: Process; Feature: Projectaddprocess Management; APIs: POST /project-add-process/:stagegateId; Feature: Projectcopystagegate Management; APIs: POST /project-copy-stagegate; Feature: Projectprocess Management; APIs: GET /project-processes/:stagegateId; Collections: ProjectProcess; Feature: Projectstagegate Management; Collections: ProjectStagegate; Feature: Projectstagegatestatu Management; APIs: POST /project-stagegate-status; Feature: Removeprocessesfromstagegate Management; APIs: DELETE /remove-processes-from-stagegate/:stagegateId; Feature: Stagegate Management; Collections: Stagegate; Feature: Timeline Management; APIs: GET /timeline; Feature: Timelinevalidation Management; APIs: POST /timeline-validation; Feature: Updateprojectstagegate Management; APIs: POST /update-project-stagegate; Feature: Upserttimeline Management; APIs: POST /upsert-timeline
Tags: scheduling, stagegate

### EBR-0476

Projecttotemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-344
Evidence: Generated from business-rules.json rule BR-344
Tags: document management, data, project, activity, management, projecttotemplate, documents, must, created, stored, updated, through, controlled

### EBR-0477

The system must maintain Activity Files records as source data for Activityfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-418
Evidence: Generated from business-rules.json rule BR-418
Tags: document management, data, project, activity, management, system, must, maintain, files, records, source, activityfile

### EBR-0478

The system must maintain Primavera Linkage Log records as source data for Primaveralinkagelog.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-424
Evidence: Generated from business-rules.json rule BR-424
Tags: audit, data, project, activity, management, system, must, maintain, primavera, linkage, records, source, primaveralinkagelog

### EBR-0479

The system must maintain Project Activity Files records as source data for Projectactivityfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-429
Evidence: Generated from business-rules.json rule BR-429
Tags: document management, data, project, activity, management, system, must, maintain, files, records, source, projectactivityfile

### EBR-0480

The system must maintain Project Process Files records as source data for Projectprocessfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-437
Evidence: Generated from business-rules.json rule BR-437
Tags: document management, data, project, activity, management, system, must, maintain, process, files, records, source, projectprocessfile

### EBR-0481

The system must maintain Project Sub Activity Files records as source data for Projectsubactivityfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-443
Evidence: Generated from business-rules.json rule BR-443
Tags: document management, data, project, activity, management, system, must, maintain, files, records, source, projectsubactivityfile

### EBR-0482

The system must maintain Project Task Files records as source data for Projecttaskfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-447
Evidence: Generated from business-rules.json rule BR-447
Tags: document management, data, project, activity, management, system, must, maintain, task, files, records, source, projecttaskfile

### EBR-0483

The system must maintain Sub Activity Files records as source data for Subactivityfile.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-452
Evidence: Generated from business-rules.json rule BR-452
Tags: document management, data, project, activity, management, system, must, maintain, files, records, source, subactivityfile

### EBR-0484

The system must maintain Pmweb Project records as source data for Pmwebproject.

Classification: Integration
Testing Value Score: 7
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-422
Evidence: Generated from business-rules.json rule BR-422
Tags: integration, data, project, activity, management, system, must, maintain, pmweb, records, source, pmwebproject

### EBR-0485

The system must maintain Primavera Activity records as source data for Primaveraactivity.

Classification: Integration
Testing Value Score: 7
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-423
Evidence: Generated from business-rules.json rule BR-423
Tags: integration, data, project, activity, management, system, must, maintain, primavera, records, source, primaveraactivity

### EBR-0486

The system must maintain Primavera Linkage records as source data for Primaveralinkage.

Classification: Integration
Testing Value Score: 7
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-425
Evidence: Generated from business-rules.json rule BR-425
Tags: integration, data, project, activity, management, system, must, maintain, primavera, linkage, records, source, primaveralinkage

### EBR-0487

The system must maintain Primavera Project records as source data for Primaveraproject.

Classification: Integration
Testing Value Score: 7
Business Criticality: Medium
Confidence: 0.7
Source Rule IDs: BR-426
Evidence: Generated from business-rules.json rule BR-426
Tags: integration, data, project, activity, management, system, must, maintain, primavera, records, source, primaveraproject

### EBR-0488

Project and Activity records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-376, BR-377, BR-378, BR-379, BR-380, BR-381, BR-382, BR-383, BR-384, BR-385, BR-386, BR-387, BR-388, BR-389, BR-390, BR-391, BR-392, BR-393, BR-394, BR-395, BR-396, BR-397, BR-398, BR-399, BR-400, BR-401, BR-402, BR-403, BR-409, BR-411, BR-412, BR-413, BR-416
Evidence: Consolidated 33 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0489

Project and Activity records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-334, BR-335, BR-336, BR-337, BR-338, BR-339, BR-340, BR-341, BR-342, BR-343, BR-345, BR-346, BR-347, BR-348, BR-349, BR-350, BR-351
Evidence: Consolidated 17 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0490

Project and Activity records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-404, BR-405, BR-406, BR-407, BR-408, BR-410, BR-414, BR-415
Evidence: Consolidated 8 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0491

Project and Activity records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-460, BR-461, BR-462, BR-463, BR-464, BR-465, BR-466, BR-467, BR-468, BR-469, BR-470, BR-471, BR-472, BR-473, BR-474, BR-475, BR-476, BR-477, BR-478, BR-479, BR-480, BR-481, BR-482, BR-483, BR-484, BR-485, BR-486, BR-487, BR-488, BR-489, BR-490, BR-491, BR-492, BR-493, BR-494, BR-495, BR-496
Evidence: Consolidated 37 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Reporting, Audit and Logs

### EBR-0492

Alldelegationlog work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-933
Evidence: Generated from business-rules.json rule BR-933
Tags: raci, workflow, reporting, audit, logs, alldelegationlog, work, must, have, clear, ownership, before, progress

### EBR-0493

Delegation changes must preserve original accountability and audit history.

Classification: RACI
Testing Value Score: 10
Business Criticality: High
Confidence: 0.82
Source Rule IDs: BR-932, BR-933, BR-934, BR-935, BR-936, BR-937, BR-938, BR-940, BR-942, BR-948
Evidence: Feature: Alldelegationlog Management; APIs: GET /all-delegation-logs; Feature: Delegationofauthority Management; Collections: DelegationOfAuthority; Feature: Updatedelegation Management; APIs: POST /update-delegation
Tags: raci, delegation, audit

### EBR-0494

Delegationofauthority work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-934
Evidence: Generated from business-rules.json rule BR-934
Tags: raci, workflow, reporting, audit, logs, delegationofauthority, work, must, have, clear, ownership, before, progress

### EBR-0495

The system must maintain Delegation Of Authority records as source data for Delegationofauthority.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-942
Evidence: Generated from business-rules.json rule BR-942
Tags: raci, data, reporting, audit, logs, system, must, maintain, delegation, authority, records, source, delegationofauthority

### EBR-0496

Updatedelegation work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-935
Evidence: Generated from business-rules.json rule BR-935
Tags: raci, workflow, reporting, audit, logs, updatedelegation, work, must, have, clear, ownership, before, progress

### EBR-0497

Users must select an existing Audit record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-945
Evidence: Generated from business-rules.json rule BR-945
Tags: validation, data, reporting, audit, logs, users, must, select, existing, record, before, detail, actions

### EBR-0498

Users must select an existing History record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-946
Evidence: Generated from business-rules.json rule BR-946
Tags: validation, data, reporting, audit, logs, users, must, select, existing, history, record, before, detail

### EBR-0499

Users must select an existing Summary record before detail actions are performed.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.66
Source Rule IDs: BR-947
Evidence: Generated from business-rules.json rule BR-947
Tags: validation, data, reporting, audit, logs, users, must, select, existing, summary, record, before, detail

### EBR-0500

Access to Fileaccessauditlog must be governed by user roles and permissions.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.84
Source Rule IDs: BR-932
Evidence: Generated from business-rules.json rule BR-932
Tags: audit, authorization, reporting, logs, access, fileaccessauditlog, must, governed, user, roles, permissions

### EBR-0501

Fileaccessauditlog documents must be created, stored, or updated through controlled document processes.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-936
Evidence: Generated from business-rules.json rule BR-936
Tags: audit, authorization, reporting, logs, fileaccessauditlog, documents, must, created, stored, updated, through, controlled

### EBR-0502

Filecontentauditlog documents must be created, stored, or updated through controlled document processes.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-937
Evidence: Generated from business-rules.json rule BR-937
Tags: audit, data, reporting, logs, filecontentauditlog, documents, must, created, stored, updated, through, controlled

### EBR-0503

The system must maintain Authorization Denied Audit Log records as source data for Authorizationdeniedauditlog.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-941
Evidence: Generated from business-rules.json rule BR-941
Tags: audit, authorization, reporting, logs, system, must, maintain, denied, records, source, data, authorizationdeniedauditlog

### EBR-0504

The system must maintain File Access Audit Log records as source data for Fileaccessauditlog.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-943
Evidence: Generated from business-rules.json rule BR-943
Tags: audit, authorization, reporting, logs, system, must, maintain, file, access, records, source, data

### EBR-0505

The system must maintain File Content Audit Log records as source data for Filecontentauditlog.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.7
Source Rule IDs: BR-944
Evidence: Generated from business-rules.json rule BR-944
Tags: audit, data, reporting, logs, system, must, maintain, file, content, records, source, filecontentauditlog

### EBR-0506

Version and revision changes must preserve audit history.

Classification: Audit
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-939
Evidence: Feature: Rollbackversion Management; APIs: POST /rollback-version
Tags: audit, version

### EBR-0507

Reporting, Audit and Logs records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-938, BR-939
Evidence: Consolidated 2 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0508

Reporting, Audit and Logs records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-940
Evidence: Consolidated 1 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0509

Reporting, Audit and Logs records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-948, BR-949, BR-950, BR-951, BR-952, BR-953, BR-954
Evidence: Consolidated 7 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Vendor and Organization Management

### EBR-0510

Cancelcompany lifecycle actions must be enforced through workflow endpoints.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-260
Evidence: Generated from business-rules.json rule BR-260
Tags: workflow, vendor, organization, management, cancelcompany, lifecycle, actions, must, enforced, through, endpoints

### EBR-0511

Companydetail lifecycle actions must be enforced through workflow endpoints.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-261
Evidence: Generated from business-rules.json rule BR-261
Tags: workflow, vendor, organization, management, companydetail, lifecycle, actions, must, enforced, through, endpoints

### EBR-0512

Companydetail records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-264
Evidence: Generated from business-rules.json rule BR-264
Tags: state transition, workflow, vendor, organization, management, companydetail, records, must, move, through, defined, states

### EBR-0513

Vendorsubmit lifecycle actions must be enforced through workflow endpoints.

Classification: Workflow
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-262
Evidence: Generated from business-rules.json rule BR-262
Tags: workflow, vendor, organization, management, vendorsubmit, lifecycle, actions, must, enforced, through, endpoints

### EBR-0514

Vendorsubmit records must move through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-265
Evidence: Generated from business-rules.json rule BR-265
Tags: state transition, workflow, vendor, organization, management, vendorsubmit, records, must, move, through, defined, states

### EBR-0515

Onboarding onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-252
Evidence: Generated from business-rules.json rule BR-252
Tags: validation, workflow, vendor, organization, management, onboarding, must, completed, before, active, participation

### EBR-0516

Onboardingtemplate onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-253
Evidence: Generated from business-rules.json rule BR-253
Tags: validation, workflow, vendor, organization, management, onboardingtemplate, onboarding, must, completed, before, active, participation

### EBR-0517

Sendtovendor onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-254
Evidence: Generated from business-rules.json rule BR-254
Tags: validation, workflow, vendor, organization, management, sendtovendor, onboarding, must, completed, before, active, participation

### EBR-0518

Vendoralldashboard onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-255
Evidence: Generated from business-rules.json rule BR-255
Tags: validation, workflow, vendor, organization, management, vendoralldashboard, onboarding, must, completed, before, active, participation

### EBR-0519

Vendordashboard onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-256
Evidence: Generated from business-rules.json rule BR-256
Tags: validation, workflow, vendor, organization, management, vendordashboard, onboarding, must, completed, before, active, participation

### EBR-0520

Vendorrespond onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-257
Evidence: Generated from business-rules.json rule BR-257
Tags: validation, workflow, vendor, organization, management, vendorrespond, onboarding, must, completed, before, active, participation

### EBR-0521

Vendorsave onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-258
Evidence: Generated from business-rules.json rule BR-258
Tags: validation, workflow, vendor, organization, management, vendorsave, onboarding, must, completed, before, active, participation

### EBR-0522

Vendorsubmit onboarding must be completed before active vendor participation.

Classification: Validation
Testing Value Score: 9
Business Criticality: High
Confidence: 0.83
Source Rule IDs: BR-259
Evidence: Generated from business-rules.json rule BR-259
Tags: validation, workflow, vendor, organization, management, vendorsubmit, onboarding, must, completed, before, active, participation

### EBR-0523

Onboardingtemplate documents must be created, stored, or updated through controlled document processes.

Classification: Document Management
Testing Value Score: 8
Business Criticality: High
Confidence: 0.8
Source Rule IDs: BR-263
Evidence: Generated from business-rules.json rule BR-263
Tags: document management, workflow, vendor, organization, management, onboardingtemplate, documents, must, created, stored, updated, through, controlled

### EBR-0524

Vendor and Organization records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-266, BR-267, BR-268, BR-269, BR-270, BR-271, BR-272, BR-273, BR-274, BR-275, BR-276, BR-277, BR-278, BR-279, BR-280, BR-281, BR-282, BR-283, BR-284
Evidence: Consolidated 19 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0525

Vendor and Organization records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-285, BR-286, BR-287, BR-288, BR-289, BR-290
Evidence: Consolidated 6 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve

## Workflow, Approval and RACI

### EBR-0526

Accountableinput work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-504
Evidence: Generated from business-rules.json rule BR-504
Tags: raci, workflow, approval, accountableinput, work, must, have, clear, ownership, before, progress

### EBR-0527

Approval items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-497
Evidence: Generated from business-rules.json rule BR-497
Tags: raci, workflow, approval, items, require, decision, before, completion

### EBR-0528

Approval must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-497, BR-498, BR-499, BR-500, BR-501, BR-502, BR-503, BR-543, BR-567, BR-592, BR-617, BR-631, BR-643, BR-649
Evidence: Feature: Approval Management; APIs: GET /:id/approvals, POST /:id/approval
Tags: state transition, workflow, state-transition

### EBR-0529

Approve items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-498
Evidence: Generated from business-rules.json rule BR-498
Tags: raci, workflow, approval, approve, items, require, decision, before, completion

### EBR-0530

Approve lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-505
Evidence: Generated from business-rules.json rule BR-505
Tags: raci, workflow, approval, approve, lifecycle, actions, must, enforced, through, endpoints

### EBR-0531

Ask items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-499
Evidence: Generated from business-rules.json rule BR-499
Tags: raci, workflow, approval, items, require, decision, before, completion

### EBR-0532

Ask lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-506
Evidence: Generated from business-rules.json rule BR-506
Tags: raci, workflow, approval, lifecycle, actions, must, enforced, through, endpoints

### EBR-0533

Assignraci work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-507
Evidence: Generated from business-rules.json rule BR-507
Tags: raci, workflow, approval, assignraci, work, must, have, clear, ownership, before, progress

### EBR-0534

Award documents must be created, stored, or updated through controlled document processes.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-529
Evidence: Generated from business-rules.json rule BR-529
Tags: raci, data, workflow, approval, award, documents, must, created, stored, updated, through, controlled

### EBR-0535

Award file movement must use controlled import, export, upload, or download actions.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.76
Source Rule IDs: BR-562
Evidence: Generated from business-rules.json rule BR-562
Tags: raci, technical, workflow, approval, award, file, movement, must, controlled, import, export, upload

### EBR-0536

Award lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-508
Evidence: Generated from business-rules.json rule BR-508
Tags: raci, workflow, approval, award, lifecycle, actions, must, enforced, through, endpoints

### EBR-0537

Award records must follow the applicable opportunity lifecycle.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-530
Evidence: Generated from business-rules.json rule BR-530
Tags: raci, workflow, approval, award, records, must, follow, applicable, opportunity, lifecycle

### EBR-0538

Award records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-533
Evidence: Generated from business-rules.json rule BR-533
Tags: raci, workflow, approval, award, records, must, move, through, defined, states

### EBR-0539

Cancel lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-509
Evidence: Generated from business-rules.json rule BR-509
Tags: raci, workflow, approval, cancel, lifecycle, actions, must, enforced, through, endpoints

### EBR-0540

Canceldelegation lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-510
Evidence: Generated from business-rules.json rule BR-510
Tags: raci, workflow, approval, canceldelegation, lifecycle, actions, must, enforced, through, endpoints

### EBR-0541

Canceldelegation work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-511
Evidence: Generated from business-rules.json rule BR-511
Tags: raci, workflow, approval, canceldelegation, work, must, have, clear, ownership, before, progress

### EBR-0542

Checklistinfo records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-534
Evidence: Generated from business-rules.json rule BR-534
Tags: raci, workflow, approval, checklistinfo, records, must, move, through, defined, states

### EBR-0543

Checklistlink records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-535
Evidence: Generated from business-rules.json rule BR-535
Tags: raci, workflow, approval, checklistlink, records, must, move, through, defined, states

### EBR-0544

Checklistlinktype records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-536
Evidence: Generated from business-rules.json rule BR-536
Tags: raci, workflow, approval, checklistlinktype, records, must, move, through, defined, states

### EBR-0545

Checklisttype records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-537
Evidence: Generated from business-rules.json rule BR-537
Tags: raci, workflow, approval, checklisttype, records, must, move, through, defined, states

### EBR-0546

Close lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-512
Evidence: Generated from business-rules.json rule BR-512
Tags: raci, workflow, approval, close, lifecycle, actions, must, enforced, through, endpoints

### EBR-0547

Closechecklist lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-513
Evidence: Generated from business-rules.json rule BR-513
Tags: raci, workflow, approval, closechecklist, lifecycle, actions, must, enforced, through, endpoints

### EBR-0548

Closechecklist records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-538
Evidence: Generated from business-rules.json rule BR-538
Tags: raci, workflow, approval, closechecklist, records, must, move, through, defined, states

### EBR-0549

Complete lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-514
Evidence: Generated from business-rules.json rule BR-514
Tags: raci, workflow, approval, complete, lifecycle, actions, must, enforced, through, endpoints

### EBR-0550

Complete records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-539
Evidence: Generated from business-rules.json rule BR-539
Tags: raci, workflow, approval, complete, records, must, move, through, defined, states

### EBR-0551

Completecustom lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-515
Evidence: Generated from business-rules.json rule BR-515
Tags: raci, workflow, approval, completecustom, lifecycle, actions, must, enforced, through, endpoints

### EBR-0552

Completecustom records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-540
Evidence: Generated from business-rules.json rule BR-540
Tags: raci, workflow, approval, completecustom, records, must, move, through, defined, states

### EBR-0553

Consultantcomplete lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-516
Evidence: Generated from business-rules.json rule BR-516
Tags: raci, workflow, approval, consultantcomplete, lifecycle, actions, must, enforced, through, endpoints

### EBR-0554

Consultantcomplete records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-541
Evidence: Generated from business-rules.json rule BR-541
Tags: raci, workflow, approval, consultantcomplete, records, must, move, through, defined, states

### EBR-0555

Delegatedraciassignee work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-517
Evidence: Generated from business-rules.json rule BR-517
Tags: raci, workflow, approval, delegatedraciassignee, work, must, have, clear, ownership, before, progress

### EBR-0556

Delegation changes must preserve original accountability and audit history.

Classification: RACI
Testing Value Score: 10
Business Criticality: High
Confidence: 0.82
Source Rule IDs: BR-509, BR-510, BR-511, BR-573, BR-574, BR-575, BR-634
Evidence: Feature: Canceldelegation Management; APIs: POST /cancel-delegation
Tags: raci, delegation, audit

### EBR-0557

Deletechecklist records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-542
Evidence: Generated from business-rules.json rule BR-542
Tags: raci, workflow, approval, deletechecklist, records, must, move, through, defined, states

### EBR-0558

Executionapproval items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-500
Evidence: Generated from business-rules.json rule BR-500
Tags: raci, workflow, approval, executionapproval, items, require, decision, before, completion

### EBR-0559

Executionapproval must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-497, BR-498, BR-499, BR-500, BR-501, BR-502, BR-503, BR-543, BR-544, BR-545, BR-546, BR-547, BR-548, BR-549, BR-550, BR-564, BR-567, BR-617, BR-618, BR-619, BR-620, BR-621, BR-622, BR-623, BR-624, BR-631, BR-643
Evidence: Feature: Executionapproval Management; Collections: ExecutionApproval
Tags: state transition, workflow, state-transition

### EBR-0560

Executionapproval records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-543
Evidence: Generated from business-rules.json rule BR-543
Tags: raci, workflow, approval, executionapproval, records, must, move, through, defined, states

### EBR-0561

Executionattachment records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-544
Evidence: Generated from business-rules.json rule BR-544
Tags: raci, workflow, approval, executionattachment, records, must, move, through, defined, states

### EBR-0562

Executionclosure records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-545
Evidence: Generated from business-rules.json rule BR-545
Tags: raci, workflow, approval, executionclosure, records, must, move, through, defined, states

### EBR-0563

Executioninitiation records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-546
Evidence: Generated from business-rules.json rule BR-546
Tags: raci, workflow, approval, executioninitiation, records, must, move, through, defined, states

### EBR-0564

Executionlog records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-547
Evidence: Generated from business-rules.json rule BR-547
Tags: raci, workflow, approval, executionlog, records, must, move, through, defined, states

### EBR-0565

Executionmaster changes must be managed through administrative controls.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.74
Source Rule IDs: BR-564
Evidence: Generated from business-rules.json rule BR-564
Tags: raci, business, workflow, approval, executionmaster, changes, must, managed, through, administrative, controls

### EBR-0566

Executionmaster records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-548
Evidence: Generated from business-rules.json rule BR-548
Tags: raci, workflow, approval, executionmaster, records, must, move, through, defined, states

### EBR-0567

Executionreviewconsult records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-549
Evidence: Generated from business-rules.json rule BR-549
Tags: raci, workflow, approval, executionreviewconsult, records, must, move, through, defined, states

### EBR-0568

Executionstep records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-550
Evidence: Generated from business-rules.json rule BR-550
Tags: raci, workflow, approval, executionstep, records, must, move, through, defined, states

### EBR-0569

Generateworkflow must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-505, BR-506, BR-508, BR-509, BR-510, BR-512, BR-513, BR-514, BR-515, BR-516, BR-520, BR-521, BR-523, BR-525, BR-526, BR-533, BR-534, BR-535, BR-536, BR-537, BR-538, BR-539, BR-540, BR-541, BR-542, BR-543, BR-544, BR-545, BR-546, BR-547, BR-548, BR-549, BR-550, BR-551, BR-552, BR-553, BR-554, BR-555, BR-556, BR-557, BR-558, BR-559, BR-560, BR-585
Evidence: Feature: Generateworkflow Management; APIs: POST /generate-workflow
Tags: state transition, workflow, state-transition

### EBR-0570

Generateworkflow records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-551
Evidence: Generated from business-rules.json rule BR-551
Tags: raci, workflow, approval, generateworkflow, records, must, move, through, defined, states

### EBR-0571

Newchecklist records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-552
Evidence: Generated from business-rules.json rule BR-552
Tags: raci, workflow, approval, newchecklist, records, must, move, through, defined, states

### EBR-0572

Only Accountable users may approve workflow items.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.9
Source Rule IDs: BR-497, BR-498, BR-499, BR-500, BR-501, BR-502, BR-503, BR-504, BR-505, BR-506, BR-507, BR-517, BR-518, BR-519, BR-520, BR-521, BR-522, BR-523, BR-524, BR-527, BR-532, BR-542, BR-543, BR-544, BR-545, BR-546, BR-547, BR-548, BR-549, BR-550, BR-554, BR-564, BR-565, BR-567, BR-568, BR-569, BR-570, BR-571, BR-583, BR-588, BR-589, BR-592, BR-597, BR-598, BR-600, BR-607, BR-608, BR-613, BR-616, BR-617, BR-618, BR-619, BR-620, BR-621, BR-622, BR-623, BR-624, BR-626, BR-627, BR-628, BR-629, BR-631, BR-632, BR-633, BR-637, BR-638, BR-640, BR-643, BR-644, BR-649, BR-652
Evidence: Feature: Accountableinput Management; APIs: POST /accountable-input; Feature: Approval Management; APIs: GET /:id/approvals, POST /:id/approval; Feature: Approve Management; APIs: POST /:id/approve, POST /approve; Feature: Ask Management; APIs: DELETE /:id/asks/:askId, GET /:bookingId/asks/:askId, GET /:meetingId/asks, POST /:id/asks, POST /:id/asks/:askId/abstain, POST /:id/asks/:askId/approve, POST /:id/asks/:askId/reject, PUT /:id/asks/:askId/outcome; Collections: Ask; Feature: Assignraci Management; APIs: POST /assign-raci; Feature: Delegatedraciassignee Management; Collections: DelegatedRaciAssignees; Feature: Executionapproval Management; Collections: ExecutionApproval; Feature: Raciassignee Management; Collections: RaciAssignees; Feature: Raciassignmentlog Management; Collections: RaciAssignmentLog; Feature: Removeraciassignee Management; APIs: POST /remove-raci-assignee; Feature: Slot Management; APIs: DELETE /:id/slots/:slotId, POST /:id/slots, POST /:id/slots/:slotId/suggest, PUT /:id/slots/:slotId/approve, PUT /:id/slots/:slotId/reject; Collections: Slot; Feature: Stagedraciassignee Management; Collections: StagedRaciAssignees
Tags: raci, approval, accountable

### EBR-0573

Processchecklist records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-553
Evidence: Generated from business-rules.json rule BR-553
Tags: raci, workflow, approval, processchecklist, records, must, move, through, defined, states

### EBR-0574

Raciassignee work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-518
Evidence: Generated from business-rules.json rule BR-518
Tags: raci, workflow, approval, raciassignee, work, must, have, clear, ownership, before, progress

### EBR-0575

Raciassignmentlog work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-519
Evidence: Generated from business-rules.json rule BR-519
Tags: raci, workflow, approval, raciassignmentlog, work, must, have, clear, ownership, before, progress

### EBR-0576

Reject items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-501
Evidence: Generated from business-rules.json rule BR-501
Tags: raci, workflow, approval, reject, items, require, decision, before, completion

### EBR-0577

Reject lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-520
Evidence: Generated from business-rules.json rule BR-520
Tags: raci, workflow, approval, reject, lifecycle, actions, must, enforced, through, endpoints

### EBR-0578

Rejectstep items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-502
Evidence: Generated from business-rules.json rule BR-502
Tags: raci, workflow, approval, rejectstep, items, require, decision, before, completion

### EBR-0579

Rejectstep lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-521
Evidence: Generated from business-rules.json rule BR-521
Tags: raci, workflow, approval, rejectstep, lifecycle, actions, must, enforced, through, endpoints

### EBR-0580

Rejectstep records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-554
Evidence: Generated from business-rules.json rule BR-554
Tags: raci, workflow, approval, rejectstep, records, must, move, through, defined, states

### EBR-0581

Removeraciassignee work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-522
Evidence: Generated from business-rules.json rule BR-522
Tags: raci, workflow, approval, removeraciassignee, work, must, have, clear, ownership, before, progress

### EBR-0582

Skipstep documents must be created, stored, or updated through controlled document processes.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.8
Source Rule IDs: BR-531
Evidence: Generated from business-rules.json rule BR-531
Tags: raci, data, workflow, approval, skipstep, documents, must, created, stored, updated, through, controlled

### EBR-0583

Skipstep file movement must use controlled import, export, upload, or download actions.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.76
Source Rule IDs: BR-563
Evidence: Generated from business-rules.json rule BR-563
Tags: raci, technical, workflow, approval, skipstep, file, movement, must, controlled, import, export, upload

### EBR-0584

Skipstep records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-555
Evidence: Generated from business-rules.json rule BR-555
Tags: raci, workflow, approval, skipstep, records, must, move, through, defined, states

### EBR-0585

Slot items require an approval decision before completion.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-503
Evidence: Generated from business-rules.json rule BR-503
Tags: raci, workflow, approval, slot, items, require, decision, before, completion

### EBR-0586

Slot lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-523
Evidence: Generated from business-rules.json rule BR-523
Tags: raci, workflow, approval, slot, lifecycle, actions, must, enforced, through, endpoints

### EBR-0587

Stagedraciassignee work must have clear ownership before it can progress.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-524
Evidence: Generated from business-rules.json rule BR-524
Tags: raci, workflow, approval, stagedraciassignee, work, must, have, clear, ownership, before, progress

### EBR-0588

Stepdetail records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-556
Evidence: Generated from business-rules.json rule BR-556
Tags: raci, workflow, approval, stepdetail, records, must, move, through, defined, states

### EBR-0589

Steptype records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-557
Evidence: Generated from business-rules.json rule BR-557
Tags: raci, workflow, approval, steptype, records, must, move, through, defined, states

### EBR-0590

Submit lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-525
Evidence: Generated from business-rules.json rule BR-525
Tags: raci, workflow, approval, submit, lifecycle, actions, must, enforced, through, endpoints

### EBR-0591

Submit records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-558
Evidence: Generated from business-rules.json rule BR-558
Tags: raci, workflow, approval, submit, records, must, move, through, defined, states

### EBR-0592

Submitsteptemplate lifecycle actions must be enforced through workflow endpoints.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.82
Source Rule IDs: BR-526
Evidence: Generated from business-rules.json rule BR-526
Tags: raci, workflow, approval, submitsteptemplate, lifecycle, actions, must, enforced, through, endpoints

### EBR-0593

Submitsteptemplate records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-559
Evidence: Generated from business-rules.json rule BR-559
Tags: raci, workflow, approval, submitsteptemplate, records, must, move, through, defined, states

### EBR-0594

The system must maintain Ask records as source data for Ask.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-613
Evidence: Generated from business-rules.json rule BR-613
Tags: raci, data, workflow, approval, system, must, maintain, records, source

### EBR-0595

The system must maintain Checklist Link Types records as source data for Checklistlinktype.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-614
Evidence: Generated from business-rules.json rule BR-614
Tags: raci, data, workflow, approval, system, must, maintain, checklist, link, types, records, source

### EBR-0596

The system must maintain Checklist Links records as source data for Checklistlink.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-615
Evidence: Generated from business-rules.json rule BR-615
Tags: raci, data, workflow, approval, system, must, maintain, checklist, links, records, source, checklistlink

### EBR-0597

The system must maintain Delegated Raci Assignees records as source data for Delegatedraciassignee.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-616
Evidence: Generated from business-rules.json rule BR-616
Tags: raci, data, workflow, approval, system, must, maintain, delegated, assignees, records, source, delegatedraciassignee

### EBR-0598

The system must maintain Execution Approval records as source data for Executionapproval.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-617
Evidence: Generated from business-rules.json rule BR-617
Tags: raci, workflow, approval, system, must, maintain, execution, records, source, data, executionapproval

### EBR-0599

The system must maintain Execution Attachments records as source data for Executionattachment.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-618
Evidence: Generated from business-rules.json rule BR-618
Tags: raci, data, workflow, approval, system, must, maintain, execution, attachments, records, source, executionattachment

### EBR-0600

The system must maintain Execution Closure records as source data for Executionclosure.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-619
Evidence: Generated from business-rules.json rule BR-619
Tags: raci, data, workflow, approval, system, must, maintain, execution, closure, records, source, executionclosure

### EBR-0601

The system must maintain Execution Initiation records as source data for Executioninitiation.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-620
Evidence: Generated from business-rules.json rule BR-620
Tags: raci, data, workflow, approval, system, must, maintain, execution, initiation, records, source, executioninitiation

### EBR-0602

The system must maintain Execution Log records as source data for Executionlog.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-621
Evidence: Generated from business-rules.json rule BR-621
Tags: raci, data, workflow, approval, system, must, maintain, execution, records, source, executionlog

### EBR-0603

The system must maintain Execution Master records as source data for Executionmaster.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-622
Evidence: Generated from business-rules.json rule BR-622
Tags: raci, data, workflow, approval, system, must, maintain, execution, master, records, source, executionmaster

### EBR-0604

The system must maintain Execution Review Consult records as source data for Executionreviewconsult.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-623
Evidence: Generated from business-rules.json rule BR-623
Tags: raci, data, workflow, approval, system, must, maintain, execution, review, consult, records, source

### EBR-0605

The system must maintain Execution Step records as source data for Executionstep.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-624
Evidence: Generated from business-rules.json rule BR-624
Tags: raci, data, workflow, approval, system, must, maintain, execution, step, records, source, executionstep

### EBR-0606

The system must maintain Process Checklist records as source data for Processchecklist.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-625
Evidence: Generated from business-rules.json rule BR-625
Tags: raci, data, workflow, approval, system, must, maintain, process, checklist, records, source, processchecklist

### EBR-0607

The system must maintain Raci Assignees records as source data for Raciassignee.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-626
Evidence: Generated from business-rules.json rule BR-626
Tags: raci, data, workflow, approval, system, must, maintain, assignees, records, source, raciassignee

### EBR-0608

The system must maintain Raci Assignment Log records as source data for Raciassignmentlog.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-627
Evidence: Generated from business-rules.json rule BR-627
Tags: raci, data, workflow, approval, system, must, maintain, assignment, records, source, raciassignmentlog

### EBR-0609

The system must maintain Slot records as source data for Slot.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-628
Evidence: Generated from business-rules.json rule BR-628
Tags: raci, data, workflow, approval, system, must, maintain, slot, records, source

### EBR-0610

The system must maintain Staged Raci Assignees records as source data for Stagedraciassignee.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.7
Source Rule IDs: BR-629
Evidence: Generated from business-rules.json rule BR-629
Tags: raci, data, workflow, approval, system, must, maintain, staged, assignees, records, source, stagedraciassignee

### EBR-0611

Updatestatu must progress through defined workflow states.

Classification: State Transition
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.86
Source Rule IDs: BR-529, BR-531, BR-560, BR-561, BR-570, BR-574, BR-589, BR-594, BR-608, BR-612
Evidence: Feature: Updatestatu Management; APIs: POST /update-status
Tags: state transition, workflow, state-transition

### EBR-0612

Updatestatu records must move through defined workflow states.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-560
Evidence: Generated from business-rules.json rule BR-560
Tags: raci, workflow, approval, updatestatu, records, must, move, through, defined, states

### EBR-0613

Updatestatu status must be maintained for each tracked record.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.78
Source Rule IDs: BR-561
Evidence: Generated from business-rules.json rule BR-561
Tags: raci, workflow, approval, updatestatu, status, must, maintained, each, tracked, record

### EBR-0614

Users must select an existing Actionitem record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-630
Evidence: Generated from business-rules.json rule BR-630
Tags: raci, data, workflow, approval, users, must, select, existing, actionitem, record, before, detail

### EBR-0615

Users must select an existing Approval record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-631
Evidence: Generated from business-rules.json rule BR-631
Tags: raci, workflow, approval, users, must, select, existing, record, before, detail, actions, performed

### EBR-0616

Users must select an existing Approve record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-632
Evidence: Generated from business-rules.json rule BR-632
Tags: raci, workflow, approval, users, must, select, existing, approve, record, before, detail, actions

### EBR-0617

Users must select an existing Ask record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-633
Evidence: Generated from business-rules.json rule BR-633
Tags: raci, data, workflow, approval, users, must, select, existing, record, before, detail, actions

### EBR-0618

Users must select an existing Cancel record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-634
Evidence: Generated from business-rules.json rule BR-634
Tags: raci, data, workflow, approval, users, must, select, existing, cancel, record, before, detail

### EBR-0619

Users must select an existing Close record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-635
Evidence: Generated from business-rules.json rule BR-635
Tags: raci, data, workflow, approval, users, must, select, existing, close, record, before, detail

### EBR-0620

Users must select an existing Initiate record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-636
Evidence: Generated from business-rules.json rule BR-636
Tags: raci, data, workflow, approval, users, must, select, existing, initiate, record, before, detail

### EBR-0621

Users must select an existing Meetingoutcome record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-637
Evidence: Generated from business-rules.json rule BR-637
Tags: raci, data, workflow, approval, users, must, select, existing, meetingoutcome, record, before, detail

### EBR-0622

Users must select an existing Reject record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-638
Evidence: Generated from business-rules.json rule BR-638
Tags: raci, data, workflow, approval, users, must, select, existing, reject, record, before, detail

### EBR-0623

Users must select an existing Restore record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-639
Evidence: Generated from business-rules.json rule BR-639
Tags: raci, data, workflow, approval, users, must, select, existing, restore, record, before, detail

### EBR-0624

Users must select an existing Slot record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-640
Evidence: Generated from business-rules.json rule BR-640
Tags: raci, data, workflow, approval, users, must, select, existing, slot, record, before, detail

### EBR-0625

Users must select an existing Submit record before detail actions are performed.

Classification: RACI
Testing Value Score: 10
Business Criticality: Critical
Confidence: 0.66
Source Rule IDs: BR-641
Evidence: Generated from business-rules.json rule BR-641
Tags: raci, data, workflow, approval, users, must, select, existing, submit, record, before, detail

### EBR-0626

Mandatory checklist items must be completed before workflow progression.

Classification: Validation
Testing Value Score: 9
Business Criticality: Critical
Confidence: 0.88
Source Rule IDs: BR-512, BR-513, BR-529, BR-531, BR-534, BR-535, BR-536, BR-537, BR-538, BR-542, BR-552, BR-553, BR-576, BR-577, BR-583, BR-587, BR-590, BR-614, BR-615, BR-625, BR-635, BR-646, BR-647, BR-649, BR-650
Evidence: Feature: Checklistinfo Management; APIs: GET /checklist-info; Feature: Checklistlink Management; Collections: ChecklistLinks; Feature: Checklistlinktype Management; Collections: ChecklistLinkTypes; Feature: Checklisttype Management; APIs: GET /checklist-types; Feature: Closechecklist Management; APIs: POST /close-checklist; Feature: Deletechecklist Management; APIs: POST /delete-checklist; Feature: Newchecklist Management; APIs: POST /new-checklist; Feature: Processchecklist Management; Collections: ProcessChecklist
Tags: validation, checklist, mandatory, workflow

### EBR-0627

Workflow, Approval and RACI records must be created through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-565, BR-566, BR-567, BR-568, BR-569, BR-571, BR-572, BR-573, BR-575, BR-576, BR-577, BR-578, BR-579, BR-580, BR-581, BR-582, BR-583, BR-584, BR-585, BR-586, BR-587, BR-588, BR-590, BR-591, BR-592, BR-593, BR-595, BR-596, BR-597, BR-598, BR-599, BR-600, BR-601, BR-602, BR-603, BR-604, BR-605, BR-606, BR-607, BR-609, BR-610, BR-611, BR-612
Evidence: Consolidated 43 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, create

### EBR-0628

Workflow, Approval and RACI records must be deleted only through explicit authorization through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.8
Source Rule IDs: BR-527, BR-528, BR-532
Evidence: Consolidated 3 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, delete

### EBR-0629

Workflow, Approval and RACI records must be updated through controlled system actions.

Classification: CRUD
Testing Value Score: 2
Business Criticality: Medium
Confidence: 0.72
Source Rule IDs: BR-570, BR-574, BR-589, BR-594, BR-608
Evidence: Consolidated 5 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, update

### EBR-0630

Workflow, Approval and RACI records must be retrieved through controlled system actions.

Classification: CRUD
Testing Value Score: 1
Business Criticality: Low
Confidence: 0.64
Source Rule IDs: BR-642, BR-643, BR-644, BR-645, BR-646, BR-647, BR-648, BR-649, BR-650, BR-651, BR-652, BR-653, BR-654
Evidence: Consolidated 13 repetitive CRUD rule(s).
Tags: crud, consolidated-crud, retrieve
