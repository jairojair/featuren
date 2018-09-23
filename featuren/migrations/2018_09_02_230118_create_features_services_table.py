from orator.migrations import Migration


class CreateFeaturesServicesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("features_services") as table:

            table.increments("id")

            table.unique(["feature_id", "service_id"])

            table.string("feature_id")
            table.foreign("feature_id").references("id").on("features").on_delete(
                "cascade"
            )

            table.integer("service_id")
            table.foreign("service_id").references("id").on("services").on_delete(
                "cascade"
            )

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("features_services")
