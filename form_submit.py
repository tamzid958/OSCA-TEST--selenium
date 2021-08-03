from config import driver, test_link_for_form_submit
import json
from time import sleep


def form_submit(f):
    data = json.load(f)
    input_fields = data["input_fields"]

    find_submit_btn_by = data["find_submit_btn_by"]
    submit_btn = data["submit_btn"]
    given_values = data["total_test"]

    for i in range(given_values):
        for obj in input_fields:

            find_element_by = obj["find_element_by"]
            find_element_by_value = obj["find_element_by_value"]
            values = obj["values"]

            if find_element_by == "name":
                driver.find_element_by_name(
                    find_element_by_value).send_keys(values[i])
            elif find_element_by == "id":
                driver.find_element_by_id(
                    find_element_by_value).send_keys(values[i])
            elif find_element_by == "class":
                driver.find_element_by_class_name(
                    find_element_by_value).send_keys(values[i])
            else:
                print("use specific find_element_by")
                return

        driver.save_screenshot(f"./screenshots/before_submit_{i}.png")

        if find_submit_btn_by == "name":
            driver.find_element_by_name(submit_btn).click()
        if find_submit_btn_by == "id":
            driver.find_element_by_id(submit_btn).click()
        if find_submit_btn_by == "class":
            driver.find_element_by_class_name(submit_btn).click()

        sleep(2)
        driver.save_screenshot(f"./screenshots/after_submit_{i}.png")

        sleep(1)
        driver.get(test_link_for_form_submit)


if __name__ == "__main__":
    driver.get(test_link_for_form_submit)
    f = open('form_input.json')
    sleep(2)
    form_submit(f)
