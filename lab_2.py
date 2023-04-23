# facts
facts = {
    "patient": ["John"],
    "disease": ["COVID-19", "John"],
    "symptom": ["cough", "John"],
    "symptom": ["fever", "John"]
}


rules = [
    {
        "id": 1,
        "premises": [
            {"fact": "disease", "value": "COVID-19", "var": None},
            {"fact": "symptom", "value": "cough", "var": None},
            {"fact": "symptom", "value": "fever", "var": None}
        ],
        "conclusion": {"fact": "treatment", "value": "isolation", "var": None}
    },
    {
        "id": 2,
        "premises": [
            {"fact": "disease", "value": "COVID-19", "var": None},
            {"fact": "symptom", "value": "cough", "var": None},
            {"fact": "symptom", "value": "fever", "var": None},
            {"fact": "symptom", "value": "shortness of breath", "var": None}
        ],
        "conclusion": {"fact": "treatment", "value": "hospitalization", "var": None}
    }
]


def execute_rule(rule, facts):
    for premise in rule["premises"]:
        if premise["fact"] not in facts or premise["value"] not in facts[premise["fact"]]:
            return False
    conclusion = rule["conclusion"]
    if conclusion["fact"] in facts:
        facts[conclusion["fact"]].append(conclusion["value"])
    else:
        facts[conclusion["fact"]] = [conclusion["value"]]
    return True


def apply_rules(rules, facts):
    rule_applied = True
    while rule_applied:
        rule_applied = False
        for rule in rules:
            if execute_rule(rule, facts):
                rule_applied = True

if __name__ == '__main__':
    # applying rules
    apply_rules(rules, facts)

    # printing result
    print(facts)
