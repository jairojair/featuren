from orator.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id")
            table.string("username").unique()
            table.string("password")
            table.boolean("admin").default(False)

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
