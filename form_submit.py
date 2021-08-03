from config import driver, test_link
from time import sleep


class form_data:
    def __init__(self, find_element_by, find_element_by_value, value):
        self.find_element_by = find_element_by
        self.find_element_by_value = find_element_by_value
        self.value = value


def form_submit(list, find_submit_btn_by, submit_btn):
    for obj in list:
        if obj.find_element_by == "name":
            driver.find_element_by_name(
                obj.find_element_by_value).send_keys(obj.value)
        elif obj.find_element_by == "id":
            driver.find_element_by_id(
                obj.find_element_by_value).send_keys(obj.value)
        elif obj.find_element_by == "class":
            driver.find_element_by_class_name(
                obj.find_element_by_value).send_keys(obj.value)
        else:
            print("use specific find_element_by")
            return
    if find_submit_btn_by == "name":
        driver.find_element_by_name(submit_btn).submit()
    if find_submit_btn_by == "id":
        driver.find_element_by_id(submit_btn).submit()
    if find_submit_btn_by == "class":
        driver.find_element_by_class_name(submit_btn).submit()


def main():
    list = []

    print("instructions: use name, id or class for find_element_by\n \
          for find_element_by_value use css selector from html docs\n \
          for value send keystrokes for that specfic element.")

    while True:
        find_element_by = str(input(f"find_element_by: "))

        find_element_by_value = str(input(f"find_element_by_value: "))

        value = str(input(f"send key strokes: "))

        list.append(form_data(find_element_by=find_element_by,
                    find_element_by_value=find_element_by_value, value=value))

        ans = str(input("next input (y / n): "))

        if ans == "y":
            pass
        else:
            break

    find_submit_btn_by = str(
        input(f"find submit button by class, id or name: "))
    submit_btn = str(input(f"give form submit button name: "))

    form_submit(list=list, find_submit_btn_by=find_submit_btn_by,
                submit_btn=submit_btn)

    print("form submitted successfully")


if __name__ == "__main__":
    driver.get(test_link)
    sleep(10)
    main()
