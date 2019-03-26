#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def firing_msg(alert_json):
    have_instance = False
    message = "*[{}] {}*\n".format(alert_json['status'].upper(), alert_json['labels']['alertname'])
    message = message + "Labels:\n"
    if (('summary' in alert_json['annotations'] and alert_json['labels']['instance'] in alert_json['annotations']['summary'])
        or ('description' in alert_json['annotations'] and alert_json['labels']['instance'] in alert_json['annotations']['description'])):
        have_instance = True
    for key in alert_json['labels']:
        if key == 'alertname':
            continue
        elif key == 'instance' and have_instance:
            continue
        else:
            message = message + " - {0}: {1}\n".format(key, alert_json['labels'][key])
    message = message + "Annotations:\n"
    if 'summary' in alert_json['annotations'] and alert_json['annotations']:
        message = message + " - summary: {}\n".format(alert_json['annotations']['summary'])
    if 'description' in alert_json['annotations'] and alert_json['annotations']:
        message = message + " - description: {}\n".format(alert_json['annotations']['description'])
    return message

def resolved_msg(alert_json):
    message = "*[{}] {}*\n".format(alert_json['status'].upper(), alert_json['labels']['alertname'])
    message = message + " - job: {}\n".format(alert_json['labels']['job'])
    message = message + " - instance: {}\n".format(alert_json['labels']['instance'])
    return message

def alert_msg_handler(alert_json):
    result = ""
    if alert_json['status'] == 'firing':
        result = firing_msg(alert_json)
    else:
        result = resolved_msg(alert_json)
    return result