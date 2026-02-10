import schemathesis

# Load from your local swagger.yaml file
schema = schemathesis.from_path("swagger.yaml")  # <-- your YAML file here

@schema.parametrize()
def test_get_user(case):
    response = case.call_and_validate()
    assert response.status_code == 200
