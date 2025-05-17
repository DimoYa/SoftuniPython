from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    artifact_types = {"ContemporaryArtifact": ContemporaryArtifact, "RenaissanceArtifact": RenaissanceArtifact}
    collectors_types = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.artifact_types:
            raise ValueError("Unknown artifact type!")

        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        artifact = self.artifact_types[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artifact)

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.collectors_types:
            raise ValueError("Unknown collector type!")

        collector = next((c for c in self.collectors if c.name == collector_name), None)

        if collector:
            raise ValueError(f"{collector_name} has been already registered!")

        collector = self.collectors_types[collector_type](collector_name)
        self.collectors.append(collector)

        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name), None)

        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)

        if not artifact:
            return "No such artifact."

        if not any(artifact in collector.purchased_artifacts for collector in self.collectors):
            self.artifacts.remove(artifact)
            return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count = 0

        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1

        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        result = []

        sorted_collectors = sorted(self.collectors, key=lambda x: (-(len(x.purchased_artifacts)), x.name))

        result.append("**Auction statistics**")

        total_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        result.append(f"Total number of sold artifacts: {total_sold_artifacts}")
        result.append(f"Available artifacts for sale: {len(self.artifacts)}")
        result.append("***")

        for c in sorted_collectors:
            result.append(c.__str__())

        return "\n".join(result)

