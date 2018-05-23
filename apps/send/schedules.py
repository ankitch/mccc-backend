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
