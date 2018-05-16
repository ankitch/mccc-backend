from django_q.tasks import schedule


def schedule_sms(trigger_func, campaign, segment, reg_id, next_run, sch_type, repeats, minutes):
    print("===== Scheduling SMS =====")
    if sch_type == 'O':
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       reg_id=reg_id,
                       hook='apps.send.hooks.print_result',
                       schedule_type=sch_type,
                       next_run=next_run)

    elif sch_type == 'I':
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       reg_id=reg_id,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       reg_id=reg_id,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats)
    return sch
