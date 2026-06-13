import re

file_path = '/opt/cran_clean_mds/docs/gazettes/5535.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 17
content = content.replace(
    'No.293 CommunicationsRegulatoryAuthorityof Namibia:Noticeto establishthefeasibility of theutilization ofTVwhitespacesfortelecommunicationsserviccsonasecondarybasisinthe470MHZto694MHZ spectrumband allocatedtobroadcastingservicesin theRepublicofNamibia',
    'No. 293 Communications Regulatory Authority of Namibia: Notice to establish the feasibility of the utilization of TV white spaces for telecommunications services on a secondary basis in the 470 MHZ to 694 MHZ spectrum band allocated to broadcasting services in the Republic of Namibia'
)

# Fix 25
content = content.replace(
    'STUDYTOESTABLISHTHEFEASIBILITYOFTHEUTILISATIONOFTVWHITE SPACESFORTELECOMMUNICATIONSSERVICESONASECONDARYBASISINTHE SERVICESINTHEREPUBLICOFNAMIBIA',
    'STUDY TO ESTABLISH THE FEASIBILITY OF THE UTILISATION OF TV WHITE SPACES FOR TELECOMMUNICATIONS SERVICES ON A SECONDARY BASIS IN THE 470 MHZ TO 694 MHZ SPECTRUM BAND ALLOCATED TO BROADCASTING SERVICES IN THE REPUBLIC OF NAMIBIA'
)

# Fix 27
content = content.replace(
    'CommunicationsAct,2009(Act.No.8of 2009)herewith publishes the study as setoutin the Schedule.',
    'The Communications Regulatory Authority, in terms of Section 100(2)(d) and (e) of the Communications Act, 2009 (Act. No. 8 of 2009) herewith publishes the study as set out in the Schedule.'
)

# Fix 37
content = content.replace('- 11 MyDigitalBridgeFoundation', '- 1.1 MyDigitalBridgeFoundation')

# Fix 53-60
content = content.replace('- 1.1 toconduct a study', '- 3.1 toconduct a study')
content = content.replace('- 1.2 to establish working', '- 3.2 to establish working')
content = content.replace('- 1.3 to set up', '- 3.3 to set up')
content = content.replace('- 1.4 toidentifythe', '- 3.4 toidentifythe')
content = content.replace('- 1.5 toidentifythe', '- 3.5 toidentifythe')
content = content.replace('- 1.6 toestablish', '- 3.6 toestablish')
content = content.replace('- 1.7 togaininsight', '- 3.7 togaininsight')

# Fix 64-65
content = content.replace('- 1.1 The study shall commence', '- 4.1 The study shall commence')
content = content.replace('- 1.2 Thestudyshallterminate', '- 4.2 Thestudyshallterminate')

# Fix 78
content = content.replace(
    '- 6.2 of equipment type approval and "weightless" standards.',
    '- 6.2 The TVWS must only be deployed as per ITU Region 1 guidelines and approvals inclusive of equipment type approval and "weightless" standards.'
)

# Fix 80-82
content = content.replace(
    '''notice,should theprimaryusers complainaboutinterferenceandMDBfails torectify the MDBfrom theprimaryuser.''',
    '''notice, should the primary users complain about interference and MDB fails to rectify the complaint within forty eight (48) hours from date on which the complaint is received by MDB from the primary user.'''
)

# Fix 88
content = content.replace(
    '- 7.2 theservicesthroughoutthestudyand at alltimesberesponsibleforensuringthatitsdatabase, facilities and systems are suitable for the delivery of such services;',
    '- 7.2 To take all steps necessary to put itself in a position to be able to fully and properly provide the services throughout the study and at all times be responsible for ensuring that its database, facilities and systems are suitable for the delivery of such services;'
)

# Fix 109-113
content = content.replace('7. 7.10 MDBshall', '- 7.10 MDBshall')
content = content.replace('8. 7.11 MDBmustobtain', '- 7.11 MDBmustobtain')
content = content.replace('9. 7.12 MDBshall', '- 7.12 MDBshall')
content = content.replace('10. 7.13 MDBshall', '- 7.13 MDBshall')
content = content.replace('11. 1.14 Inaddition', '- 1.14 Inaddition')

# Fix 126
content = content.replace(
    'study',
    'study period;',
    1 # Wait, this might match the wrong 'study'. Let's do it better.
)
