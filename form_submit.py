from config import driver, test_link
import json


def form_submit():
    f = open('form_input.json')
    data = json.load(f)

    find_submit_btn_by = data["find_submit_btn_by"]
    submit_btn = data["submit_btn"]

    for obj in data["input_fields"]:

        find_element_by = obj["find_element_by"]
        find_element_by_value = obj["find_element_by_value"]
        value = obj["value"]

        if find_element_by == "name":
            driver.find_element_by_name(
                find_element_by_value).send_keys(value)
        elif find_element_by == "id":
            driver.find_element_by_id(
                find_element_by_value).send_keys(value)
        elif find_element_by == "class":
            driver.find_element_by_class_name(
                find_element_by_value).send_keys(value)
        else:
            print("use specific find_element_by")
            return
    if find_submit_btn_by == "name":
        driver.find_element_by_name(submit_btn).click()
    if find_submit_btn_by == "id":
        driver.find_element_by_id(submit_btn).click()
    if find_submit_btn_by == "class":
        driver.find_element_by_class_name(submit_btn).click()


if __name__ == "__main__":
    driver.get(test_link)
    form_submit()
