from django_q.tasks import schedule


def schedule_sms(trigger_func, name, campaign, segment, next_run, sch_type, repeats, minutes):
    if sch_type == 'O':
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run)

    elif sch_type == 'I':
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       name=name,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        sch = schedule(trigger_func,
                       campaign=campaign,
                       segment=segment,
                       name=name,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats)
    return sch


# Schedule function for email and push notification

def schedule_email_push(trigger_func, name, query, lists, next_run, sch_type, repeats, minutes):
    print(str(trigger_func))
    if sch_type == 'O':
        sch = schedule(trigger_func,
                       query=query,
                       lists=lists,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run)

    elif sch_type == 'I':
        sch = schedule(trigger_func,
                       query=query,
                       lists=lists,
                       name=name,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats, minutes=minutes)

    else:
        sch = schedule(trigger_func,
                       query=query,
                       lists=lists,
                       name=name,
                       hook='apps.send.hooks.print_result', schedule_type=sch_type,
                       next_run=next_run, repeats=repeats)
    return sch


def trigger_all(push_func, email_func, campaign, segment, sms_func, name, query, lists, next_run, sch_type, repeats,
                minutes):
    schedule_sms(sms_func, name, campaign, segment, next_run, sch_type, repeats, minutes)
    schedule_email_push(email_func, name, query, lists, next_run, sch_type, repeats, minutes)
    schedule_email_push(push_func, name, query, lists, next_run, sch_type, repeats, minutes)
