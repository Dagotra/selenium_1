from elements.button import Button
from elements.input import Input
from elements.web_element import WebElement
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = By.ID, "file-upload"
    FILE_UPLOAD_BUTTON_LOC = By.XPATH, "//input[@id='file-upload']"
    FILE_SUBMIT_BUTTON_LOC = By.ID, "file-submit"
    UNIQUE_ELEMENT_FILE_UPLOADED_LOC = By.ID, "uploaded-files"
    TEXT_UPLOADED_LOC = By.XPATH, "//div[@id='content']//h3"
    DRAG_AND_DROP_UPLOAD_LOC = By.ID, "drag-drop-upload"
    TEXT_SUCCESS_MARK_LOC = By.XPATH, "//div[@id='drag-drop-upload']//div[@class='dz-success-mark']//span"

    def __init__(self, browser):
        super().__init__(browser)
        self.name_page = "Upload"
        self.unique_element = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Upload page -> unique element page"
        )
        self.file_upload_button = Input(
            self.browser,
            self.FILE_UPLOAD_BUTTON_LOC,
            description="Upload page -> click button 'Выберите файл'"
        )
        self.file_submit_button = Button(
            self.browser,
            self.FILE_SUBMIT_BUTTON_LOC,
            description="Upload page -> click button 'Upload'"
        )
        self.unique_element_file_uploaded = WebElement(
            self.browser,
            self.UNIQUE_ELEMENT_FILE_UPLOADED_LOC,
            description="File uploaded -> check unique element"
        )
        self.text_file_uploaded = WebElement(
            self.browser,
            self.TEXT_UPLOADED_LOC,
            description="File uploaded -> get text 'File Uploaded!'"
        )
        self.drag_and_drop_upload = WebElement(
            self.browser,
            self.DRAG_AND_DROP_UPLOAD_LOC,
            description="File upload -> click drag and drop upload"
        )
        self.text_success_mark = WebElement(
            self.browser,
            self.TEXT_SUCCESS_MARK_LOC,
            description="File upload -> drag and drop upload -> check '✔'"
        )
        self.hidden_file_input = Input(
            self.browser,
            (By.XPATH, "//input[@type='file' and @multiple='multiple']"),
            description="File upload ->"
        )

    def click_file_submit_button(self) -> None:
        self.file_submit_button.click()

    def download_file(self, file_path: str) -> None:
        self.browser.upload_file(self.FILE_UPLOAD_BUTTON_LOC, file_path)

    def get_text_file_uploaded(self) -> str:
        return self.text_file_uploaded.get_text()

    def click_drag_and_drop_upload(self) -> None:
        self.drag_and_drop_upload.click()

    def get_text_success_mark(self) -> str:
        return self.text_success_mark.get_text()

    def file_d_n_d_in_element(self, path: str) -> None:
        self.file_upload_button.send_keys(path)

    def upload_file_via_hidden_input(self, path: str) -> None:
        self.hidden_file_input.send_keys_to_hidden_input(path)
