class Supplier:
    def __init__(
        self,
        supplier_id: str, #type hint
        name: str, 
        contact_email: str
    ) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}")
        print(f"Name: {self.__name}")
        print(f"Contact email: {self.__contact_email}")