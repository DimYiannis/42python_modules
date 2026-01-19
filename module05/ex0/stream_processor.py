from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
        - Abstract base class for data processing
        - parent class for all data processors
        - enabling polymorphic behavior across different data types.
    """
    # abstract methods are methods that are defined
    # in an abstract class but do not have an implementation.
    # They serve as a blueprint for the subclasses, ensuring
    # that they provide their own implementation.

    @abstractmethod
    def process(self, data: Any) -> str:
        pass
 
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        result = "Data_Processed result: " + result
        return result


class NumericProcessor(DataProcessor):
    """
     - Processor for handling numeric data (lists of numbers).
     - Validate that input is a list containing only integers or floats
     - runtime data validation
     - calculate  statistics
    """
    def __init__(self) -> None:
        self.data = []

    def process(self, data: Any) -> str:
        if self.validate(data):
            self.data = data
            return "Validation: Numeric data verified"
        else:
            return "Alert! Data not valid"

    def validate(self, data: Any) -> bool:
        """
            _ is just a throwaway variable — Python convention: 
            _ means “I don’t care about the value”

        """
        try:
            for x in data:
                _ = x + 0
            return True
        except:
            return False


    def format_output(self, result: str) -> str:
        num = len(self.data)
        plus = sum(self.data)
        avg = plus / num
        result1 = f"Output: Processed {num} numeric values, "
        result2 = f"sum={plus}, avg={avg}"
        result = result1 + result2
        return result


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.data = ""

    def process(self, data: Any) -> str:
        if self.validate(data):
            self.data = data
            return "Validation: Text data verified"
        else:
            return "Alert! Text not valid"

    def validate(self, data: Any) -> bool:
        try:
            for x in data:
                _ = x + ""
            return True
        except:
            return False


    def format_output(self, result: str) -> str:
        num = len(self.data)
        words = len(self.data.split())
        result1 = f"Output: Processed text: {num} characters, "
        result2 = f"{words} words"
        result = result1 + result2
        return result


class LogProcessor(DataProcessor):
    """
        - handle log entries.
        - Validate input is a string
        - parse and format log entries
        based on their severity level
    """
    def __init__(self) -> None:
        self.data = ""

    def process(self, data: Any) -> str:
        if self.validate(data):
            self.data = data
            return "Validation: Log entry verified"
        else:
            return "Alert! Log input not valid"

    def validate(self, data: Any) -> bool:
        try:
            for x in data:
                _ = x + ""
            return True
        except:
            return False

    def format_output(self, result: str) -> str:
        """
         - format output based on log severity level
         - parse the log entry to detect severity level (ERROR, INFO)
         - format the output with appropriate tags and extracted message.
        """
        if self.data[:5] == "ERROR":
            result = "Output: [ALERT] ERROR level detected: " + self.data[7:]
        elif self.data[:4] == "INFO":
            result = "Output: [INFO] INFO level detected: " + self.data[6:]
        else:
            result = "Output: Unknown log level: " + self.data
        return result


if __name__ == "__main__":
    
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("\nInitializing Numeric Processor...")

    data = [1, 2, 3, "a", 5]
    num_pro = NumericProcessor()

    print(f"Processing data: {data}")
    result = num_pro.validate(data) #returns error datanot valid
    if result is False:
        print(num_pro.process(data))
    else:
        print(num_pro.process(data))
        print(f"{num_pro.process(data)}") 
        print(f"{num_pro.format_output('')}")

    print("\nInitializing Text Processor...")
    data = "Hello Nexus World"
    txt_pro = TextProcessor()
    print(f"Processing data: {data}")
    print(f"{txt_pro.process(data)}")
    print(f"{txt_pro.format_output('')}")

    print("\nInitializing Log Processor...")
    data = "INFO: Connection timeout"
    log_pro = LogProcessor()
    print(f"Processing data: {data}")
    print(f"{log_pro.process(data)}")
    print(f"{log_pro.format_output('')}")


    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    '''
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    datasets = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]
    results = []
    i = 1
    for processor, data in zip(processors, datasets):
        processor.process(data)
        print(f"Result {i}: {processor.format_output('')}")
        i += 1
'''
    datasets = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]
    i = 1
    for data in datasets:
        if num_pro.validate(data) is True:
             print(num_pro.process(data))
             print(f"Result {i}: {num_pro.format_output('')}")
        else:
            if data[:4] == "INFO":
                print(f"Result {i}: {log_pro.format_output('')}")
            elif data[:5] == "ERROR":
                print(f"Result {i}: {log_pro.format_output('')}")
            else:
                 print(f"Result {i}: {txt_pro.format_output('')}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
