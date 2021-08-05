Under some circumstances, a rule is ignored when a featurized slot is set. In this example project, note the rule:

```yml
- rule: Say goodbye anytime the user says goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye
```

There are no stories with the `goodbye` intent.

Note this story which calls an action that sets a featurized slot:

```yml
- story: appts single
  steps:
    - intent: appt
    - action: action_appt
    - slot_was_set:
        - num_appts: single
    - action: utter_appts
    - action: utter_greet
```

Duplicate the problem with the following dialog:

```
/goodbye
/appt      # if num_appts is set to a value other than "none" the following /goodbye is predicted incorrectly
/goodbye
```

Shell debug log can be view [here](debug.log)