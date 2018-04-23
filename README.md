his is a simple BufferOverflow exploit found on a SlMail server using pop3 protocol.

The other files includes the various stages of exploits.


Intially the "bof_fuzzer.py", helps to gradually locate the buffer length such that it could be exploited.

Then unique pattern can be generated with the metasploit module "pattern_create.rb", the pattern generated with it is used to find the exact position of the input length which is placed at the EIP pointer :)

Using debuggers the pattern in side the EIP is identified and the position is identified using the "pattern_offset.rb" module in metasploit.

with the position of the input location and EIP. Now its easy to exploit it.

now the list of bad characters is identified with the help of the "bof_poc2.py" which is a very simple python script ;). and further refined with the "bof_poc3.py"

Now is final phase where the exac dll must be identified. For which the mona.py modules can be used.And the jmp  address is noted for the corresponding address in nasn_shell.reb

then a simple exploit is built using the msfvenom to add the payload.

now this gives the final exploit "slmailexploit.py"


Happy Hacking :)