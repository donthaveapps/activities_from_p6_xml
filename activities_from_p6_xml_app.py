import streamlit
import pandas as pd
import numpy as np
import os
import xml.etree.ElementTree as ET
import re

def get_xml_tag_prefix(eTree_root):
    """
    Get the XML tag prefix from the root element of the Element Tree.
    """
    xml_tag_prefix = re.search(r'\{.*\}', eTree_root.tag).group(0)
    return xml_tag_prefix

def get_activities_by_tag_text(eTree_root, tag, text_list):
    '''
    Takes the root of an P6 XML tree (eTree_root), and outputs a predefined list of activities attributes as a Pandas DataFrame that has (tag) text that
    is contained within a (text_list).
    '''

    # TODO: use get_xml_tag_prefix() to get the XML tag prefix from the root element of the Element Tree.

    # Define selected_activity_df columns
    selected_activity_Name = []                       #01
    selected_activity_Id = []                         #02
    selected_activity_ObjectId = []                   #03
    selected_activity_PlannedStartDate = []           #04
    selected_activity_PlannedDuration = []            #05
    selected_activity_AtCompletionDuration = []       #06
    selected_activity_ExpectedFinishDate = []         #07
    selected_activity_StartDate = []                  #08
    selected_activity_FinishDate = []                 #09
    selected_activity_ActualStartDate = []            #10
    selected_activity_ActualDuration = []             #11
    selected_activity_ActualFinishDate = []           #12
    selected_activity_Status = []                     #13
    selected_activity_EstimatedWeight = []            #14
    selected_activity_LevelingPriority =[]            #15
    selected_activity_IsStarred = []                  #16

    for activity_item in eTree_root.iter('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}Activity'):
        for activity_item_tag in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}'+str(tag)):
            if activity_item_tag.text in text_list:
                for activity_item_Name in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}Name'):
                    selected_activity_Name.append(activity_item_Name.text)                                     #01
                for activity_item_Id in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}Id'):
                    selected_activity_Id.append(activity_item_Id.text)                                         #02
                for activity_item_ObjectId in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}ObjectId'):
                    selected_activity_ObjectId.append(activity_item_ObjectId.text)                             #03
                for activity_item_PlannedStartDate in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}PlannedStartDate'):
                    selected_activity_PlannedStartDate.append(activity_item_PlannedStartDate.text)             #04
                for activity_item_PlannedDuration in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}PlannedDuration'):
                    selected_activity_PlannedDuration.append(activity_item_PlannedDuration.text)               #05
                for activity_item_AtCompletionDuration in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}AtCompletionDuration'):
                    selected_activity_AtCompletionDuration.append(activity_item_AtCompletionDuration.text)     #06
                for activity_item_ExpectedFinishDate in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}ExpectedFinishDate'):
                    selected_activity_ExpectedFinishDate.append(activity_item_ExpectedFinishDate.text)         #07
                for activity_item_StartDate in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}StartDate'):
                    selected_activity_StartDate.append(activity_item_StartDate.text)                           #08
                for activity_item_FinishDate in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}FinishDate'):
                    selected_activity_FinishDate.append(activity_item_FinishDate.text)                         #09
                for activity_item_ActualStartDate in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}ActualStartDate'):
                    selected_activity_ActualStartDate.append(activity_item_ActualStartDate.text)               #10
                for activity_item_ActualDuration in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}ActualDuration'):
                    selected_activity_ActualDuration.append(activity_item_ActualDuration.text)                 #11
                for activity_item_ActualFinishDate in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}ActualFinishDate'):
                    selected_activity_ActualFinishDate.append(activity_item_ActualFinishDate.text)             #12
                for activity_item_Status in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}Status'):
                    selected_activity_Status.append(activity_item_Status.text)                                 #13
                for activity_item_EstimatedWeight in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}EstimatedWeight'):
                    selected_activity_EstimatedWeight.append(activity_item_EstimatedWeight.text)               #14
                for activity_item_LevelingPriority in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}LevelingPriority'):
                    selected_activity_LevelingPriority.append(activity_item_LevelingPriority.text)             #15
                for activity_item_IsStarred in activity_item.findall('{http://xmlns.oracle.com/Primavera/P6/V17.12/API/BusinessObjects}IsStarred'):
                    selected_activity_IsStarred.append(activity_item_IsStarred.text)
    
    output_df = pd.DataFrame({
        "Name": selected_activity_Name,                                   #01
        "Id": selected_activity_Id,                                       #02
        "ObjectId": selected_activity_ObjectId,                           #03
        "PlannedStartDate": selected_activity_PlannedStartDate,           #04
        "PlannedDuration": selected_activity_PlannedDuration,             #05
        "AtCompletionDuration": selected_activity_AtCompletionDuration,   #06
        "ExpectedFinishDate": selected_activity_ExpectedFinishDate,       #07
        "StartDate": selected_activity_StartDate,                         #08
        "FinishDate": selected_activity_FinishDate,                       #09
        "ActualStartDate": selected_activity_ActualStartDate,             #10
        "ActualDuration": selected_activity_ActualDuration,               #11
        "ActualFinishDate": selected_activity_ActualFinishDate,           #12
        "Status": selected_activity_Status,                               #13
        "EstimatedWeight": selected_activity_EstimatedWeight,             #14
        "Priority": selected_activity_LevelingPriority,                   #15
        "IsStarred": selected_activity_IsStarred,                         #16
    })

    return output_df

def get_ActivityCodeDict_by_Description(eTree_root, description):
    """
    This function is used to get a dict of ObjectId and CodeValue of an ActivityCode by its Description.
    """
    # Get XML tag prefix
    xml_tag_prefix = get_xml_tag_prefix(eTree_root)

    # Initialise dictionary
    output_dict = {
        "Description": description,
        "CodeValue": "",
        "ObjectId": ""
        }
    for activity_code in eTree_root.findall(xml_tag_prefix + 'ActivityCode'):
        for activity_item_Description in activity_code.findall(xml_tag_prefix + 'Description'):
            if activity_item_Description.text == description:  # This is for exact match, alternative is to use 'in'; TODO: upper/lower case
                for activity_item_CodeValue in activity_code.findall(xml_tag_prefix + 'CodeValue'):
                    output_dict["CodeValue"] = activity_item_CodeValue.text
                for activity_item_ObjectId in activity_code.findall(xml_tag_prefix + 'ObjectId'):
                    output_dict["ObjectId"] = activity_item_ObjectId.text
    return output_dict

def get_activities_by_code_ValueObjectId(eTree_root, ActivityCode_ObjectId):
    '''
    This function is used to get a list of activities by its ActivityCode_ObjectId.
    '''

    # Get XML tag prefix
    xml_tag_prefix = get_xml_tag_prefix(eTree_root)

    # Initialise list
    selected_activity_Name = []
    selected_activity_Id = []
    selected_activity_ObjectId = []
    selected_activity_PlannedStartDate = []
    selected_activity_PlannedDuration = []
    selected_activity_AtCompletionDuration = []
    selected_activity_ExpectedFinishDate = []
    selected_activity_StartDate = []
    selected_activity_FinishDate = []
    selected_activity_ActualStartDate = []
    selected_activity_ActualDuration = []
    selected_activity_ActualFinishDate = []
    selected_activity_Status = []
    selected_activity_EstimatedWeight = []
    selected_activity_LevelingPriority = []
    selected_activity_IsStarred = []

    # test_output = []
    
    for activity_item in eTree_root.iter(xml_tag_prefix + 'Activity'):
        for activity_item_Code in activity_item.findall(xml_tag_prefix + 'Code'):
            for activity_item_Code_ValueObjectId in activity_item_Code.findall(xml_tag_prefix + 'ValueObjectId'):
                if activity_item_Code_ValueObjectId.text == ActivityCode_ObjectId:
                    for activity_item_Name in activity_item.findall(xml_tag_prefix + 'Name'):
                        selected_activity_Name.append(activity_item_Name.text)                                 #01
                    for activity_item_Id in activity_item.findall(xml_tag_prefix + 'Id'):
                        selected_activity_Id.append(activity_item_Id.text)                                     #02
                    for activity_item_ObjectId in activity_item.findall(xml_tag_prefix + 'ObjectId'):
                        selected_activity_ObjectId.append(activity_item_ObjectId.text)                         #03
                    for activity_item_PlannedStartDate in activity_item.findall(xml_tag_prefix + 'PlannedStartDate'):
                        selected_activity_PlannedStartDate.append(activity_item_PlannedStartDate.text)         #04
                    for activity_item_PlannedDuration in activity_item.findall(xml_tag_prefix + 'PlannedDuration'):
                        selected_activity_PlannedDuration.append(activity_item_PlannedDuration.text)               #05
                    for activity_item_AtCompletionDuration in activity_item.findall(xml_tag_prefix + 'AtCompletionDuration'):
                        selected_activity_AtCompletionDuration.append(activity_item_AtCompletionDuration.text)     #06
                    for activity_item_ExpectedFinishDate in activity_item.findall(xml_tag_prefix + 'ExpectedFinishDate'):
                        selected_activity_ExpectedFinishDate.append(activity_item_ExpectedFinishDate.text)         #07
                    for activity_item_StartDate in activity_item.findall(xml_tag_prefix + 'StartDate'):
                        selected_activity_StartDate.append(activity_item_StartDate.text)                           #08
                    for activity_item_FinishDate in activity_item.findall(xml_tag_prefix + 'FinishDate'):
                        selected_activity_FinishDate.append(activity_item_FinishDate.text)                         #09
                    for activity_item_ActualStartDate in activity_item.findall(xml_tag_prefix + 'ActualStartDate'):
                        selected_activity_ActualStartDate.append(activity_item_ActualStartDate.text)               #10
                    for activity_item_ActualDuration in activity_item.findall(xml_tag_prefix + 'ActualDuration'):
                        selected_activity_ActualDuration.append(activity_item_ActualDuration.text)                 #11
                    for activity_item_ActualFinishDate in activity_item.findall(xml_tag_prefix + 'ActualFinishDate'):
                        selected_activity_ActualFinishDate.append(activity_item_ActualFinishDate.text)             #12
                    for activity_item_Status in activity_item.findall(xml_tag_prefix + 'Status'):
                        selected_activity_Status.append(activity_item_Status.text)                                 #13
                    for activity_item_EstimatedWeight in activity_item.findall(xml_tag_prefix + 'EstimatedWeight'):
                        selected_activity_EstimatedWeight.append(activity_item_EstimatedWeight.text)               #14
                    for activity_item_LevelingPriority in activity_item.findall(xml_tag_prefix + 'LevelingPriority'):
                        selected_activity_LevelingPriority.append(activity_item_LevelingPriority.text)             #15
                    for activity_item_IsStarred in activity_item.findall(xml_tag_prefix + 'IsStarred'):
                        selected_activity_IsStarred.append(activity_item_IsStarred.text)
    
    output_df = pd.DataFrame({
        "Name": selected_activity_Name,                                   #01
        "Id": selected_activity_Id,                                       #02
        "ObjectId": selected_activity_ObjectId,                           #03
        "PlannedStartDate": selected_activity_PlannedStartDate,           #04
        "PlannedDuration": selected_activity_PlannedDuration,             #05
        "AtCompletionDuration": selected_activity_AtCompletionDuration,   #06
        "ExpectedFinishDate": selected_activity_ExpectedFinishDate,       #07
        "StartDate": selected_activity_StartDate,                         #08
        "FinishDate": selected_activity_FinishDate,                       #09
        "ActualStartDate": selected_activity_ActualStartDate,             #10
        "ActualDuration": selected_activity_ActualDuration,               #11
        "ActualFinishDate": selected_activity_ActualFinishDate,           #12
        "Status": selected_activity_Status,                               #13
        "EstimatedWeight": selected_activity_EstimatedWeight,             #14
        "Priority": selected_activity_LevelingPriority,                   #15
        "IsStarred": selected_activity_IsStarred,                         #16
    })

    return output_df

## Method 1: Keyword search in activity code (e.g. "DN")

## Method 2: Keyword search in WBS