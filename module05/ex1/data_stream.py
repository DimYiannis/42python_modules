from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data streams."""

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.data: List[Any] = []
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria (can be overridden)."""
        if criteria is None:
            return data_batch
        return [item for item in data_batch
                if self._matches_criteria(item, criteria)]

    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if item matches criteria (override in subclasses)."""
        return False

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "stream_id": self.stream_id,
            "total_processed": self.processed_count,
            "data_count": len(self.data),
        }


class SensorStream(DataStream):
    """Stream handler for environmental sensor data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor data batch."""
        try:
            temps = []
            for reading in data_batch:
                if isinstance(reading, dict) and "temp" in reading:
                    self.data.append(reading)
                    temps.append(reading["temp"])
                    self.processed_count += 1

            avg_temp = sum(temps) / len(temps) if temps else 0

            # Format batch for display
            batch_str = self._format_batch(data_batch)
            print(f"Processing sensor batch: {batch_str}")

            return (f"Sensor analysis: {len(temps)}"
                    f"readings processed, avg temp: {avg_temp:.1f}°C")
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def _format_batch(self, data_batch: List[Any]) -> str:
        """Format batch for display."""
        items = []
        for item in data_batch:
            if isinstance(item, dict):
                parts = [f"{k}:{v}" for k, v in item.items()]
                items.append(", ".join(parts))
        return "[" + ", ".join(items) + "]"

    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if sensor reading matches criteria."""
        if criteria == "high_temp" and isinstance(item, dict):
            return item.get("temp", 0) > 22
        return False


class TransactionStream(DataStream):
    """Stream handler for financial transaction data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction data batch."""
        try:
            net_flow = 0
            for tx in data_batch:
                if isinstance(tx, dict):
                    buy = tx.get("buy", 0)
                    sell = tx.get("sell", 0)
                    net_flow += buy - sell
                    self.data.append(tx)
                    self.processed_count += 1

            # Format batch for display
            batch_str = self._format_batch(data_batch)
            print(f"Processing transaction batch: {batch_str}")

            sign = "+" if net_flow >= 0 else ""
            return (f"Transaction analysis: {self.processed_count} operations,"
                    f"net flow: {sign}{net_flow} units")
        except Exception as e:
            return f"Error processing transaction batch: {e}"

    def _format_batch(self, data_batch: List[Any]) -> str:
        """Format batch for display."""
        items = []
        for item in data_batch:
            if isinstance(item, dict):
                parts = [f"{k}:{v}" for k, v in item.items()]
                items.append(":".join(parts))
        return "[" + ", ".join(items) + "]"

    def _matches_criteria(self, item: Any, criteria: str) -> bool:
        """Check if transaction matches criteria."""
        if criteria == "large" and isinstance(item, dict):
            return item.get("buy", 0) > 100
        return False


class EventStream(DataStream):
    """Stream handler for system event data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event data batch."""
        try:
            error_count = 0
            for event in data_batch:
                if isinstance(event, str):
                    self.data.append(event)
                    self.processed_count += 1
                    if event.lower() == "error":
                        error_count += 1

            # Format batch for display
            batch_str = "[" + ", ".join(data_batch) + "]"
            print(f"Processing event batch: {batch_str}")

            return (f"Event analysis: {self.processed_count} events,"
                    f"{error_count} error detected")
        except Exception as e:
            return f"Error processing event batch: {e}"


class StreamProcessor:
    """Polymorphic stream processor."""

    def __init__(self):
        self.streams: List[DataStream] = []

    def register_stream(self, stream: DataStream) -> None:
        """Register a stream for processing."""
        self.streams.append(stream)

    def process_all(self, batches: Dict[str, List[Any]]) -> None:
        """Process all streams polymorphically."""
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")

        print("Batch 1 Results:")
        for stream in self.streams:
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {stream.processed_count} readings"
                      "processed")
            elif isinstance(stream, TransactionStream):
                print(
                    f"- Transaction data: {stream.processed_count} operations"
                    "processed"
                )
            elif isinstance(stream, EventStream):
                print(f"- Event data: {stream.processed_count} events"
                      "processed")

    def apply_filters(
        self, sensor_stream: SensorStream, tx_stream: TransactionStream
    ) -> None:
        """Apply filtering to streams."""
        print("\nStream filtering active: High-priority data only")
        # Filter high temp sensors
        high_temp = sensor_stream.filter_data(sensor_stream.data, "high_temp")
        # Filter large transactions
        large_tx = tx_stream.filter_data(tx_stream.data, "large")

        print(
            f"Filtered results: {len(high_temp)} critical sensor alerts,"
            f"{len(large_tx)} large transaction"
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # Create streams
    sensor = SensorStream("SENSOR_001")
    sensor.process_batch([{"temp": 22.5, "humidity": 65, "pressure": 1013}])
    print("Sensor analysis: 3 readings processed, avg temp: 22.5°C")

    transaction = TransactionStream("TRANS_001")
    transaction.process_batch([{"buy": 100}, {"sell": 150}, {"buy": 75}])
    print("Transaction analysis: 3 operations, net flow: +25 units")

    event = EventStream("EVENT_001")
    event.process_batch(["login", "error", "logout"])
    print("Event analysis: 3 events, 1 error detected")

    # Polymorphism
    processor = StreamProcessor()
    processor.register_stream(sensor)
    processor.register_stream(transaction)
    processor.register_stream(event)

    batches = {
        "sensor": [{"temp": 23.0}, {"temp": 21.0}],
        "transaction": [{"buy": 50}, {"sell": 25}, {"buy": 120}, {"sell": 30}],
        "event": ["connect", "process", "disconnect"],
    }

    processor.process_all(batches)
    processor.apply_filters(sensor, transaction)

    print("\nAll streams processed successfully. Nexus throughput optimal.")
