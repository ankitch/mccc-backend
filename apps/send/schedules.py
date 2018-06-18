from django_q.tasks import schedule


def schedule_sms(trigger_func, campaign, segment, fcm_registration_id, next_run, schedule_type, repeats, minutes):
    print("===== Scheduling SMS =====")
    if schedule_type == 'O':
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       fcm_registration_id=fcm_registration_id,
                       hook='apps.send.hooks.print_result',
                       schedule_type=schedule_type,
                       next_run=next_run)

    elif schedule_type == 'I':
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       fcm_registration_id=fcm_registration_id,
                       hook='apps.send.hooks.print_result', schedule_type=schedule_type,
                       next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       fcm_registration_id=fcm_registration_id,
                       hook='apps.send.hooks.print_result', schedule_type=schedule_type,
                       next_run=next_run, repeats=repeats)
    return sch


def schedule_email_push(trigger_func, query, lists, campaigns, next_run, sch_type, repeats, minutes):
    print("===== Scheduling Email or push =====")
    if sch_type == 'O':
        sch = schedule(trigger_func,
                       query=query,
                       lists=lists,
                       campaign=campaigns,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run)

    elif sch_type == 'I':
        sch = schedule(trigger_func,
                       query=query,
                       lists=lists,
                       campaign=campaigns,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        sch = schedule(trigger_func,
                       query=query,
                       lists=lists,
                       campaign=campaigns,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats)
    return sch


def trigger_all(push_func, email_func, sms_func, campaign, segment, query, lists, next_run, sch_type, repeats,
                minutes):
    schedule_sms(sms_func, campaign, segment, next_run, sch_type, repeats, minutes)
    schedule_email_push(email_func, query, lists, campaign, next_run, sch_type, repeats, minutes)
