from orator.migrations import Migration


class CreateFeaturesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("features") as table:
            table.string("id").unique()
            table.string("version")
            table.boolean("enabled").default(False)
            table.boolean("deny").default(False)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("features")
