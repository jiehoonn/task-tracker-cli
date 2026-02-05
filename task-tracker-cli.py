import cmd

class TaskTracker(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to TaskTracker CLI. Type "help" for any available commands.'

    def preloop(self):
        """
        The preloop method is executed once before the CLI loop starts. You can use 
        it for any setup or initialization tasks that need to happen before processing 
        commands.
        """
        # Add custom initialization code here.
        print("Initialization before the CLI loop.")

    def postloop(self):
        """
        The postloop method is executed once when the CLI is about to return. It's ideal for 
        performing cleanup or finalization tasks before your CLI exits
        """
        # Add custom initialization code here.
        print("Finalization after the CLI loop.")

    def precmd(self, line):
        """
        The precmd method is a hook that runs just before a command is executed. 
        You can use it to perform actions or checks before the command is processed.
        """

        # Add custom code here.
        print("Before command execution.")
        return line # You must return the original or modified line.
    
    def postcmd(self, stop, line):
        """
        The postcmd method runs just after a command is executed. It's useful 
        for performing actions or checks after the command has been processed.
        """

        # Add custom code here.
        print("After command execution.")
        # stop = False (continues), stop = True (exits)
        return stop # Return 'stop' to control whether the CLI stops or continues.

    def do_hello(self, line):
        """Print a Greeting"""
        print("Hello World")
    
    def do_quit(self, line):
        """Exit CLI"""
        return True

if __name__ == '__main__':
    TaskTracker().cmdloop()
