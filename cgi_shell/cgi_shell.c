#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

void startShell(int read_fd, int write_fd)
{
  printf("start shell\n");
  setsid();
  dup2(read_fd, 0);
  dup2(write_fd, 1);
  dup2(write_fd, 2);
  execve("/bin/sh", 0, 0);
  exit(0);
}

void initbash()
{
  int pipe0[2];
  int pipe1[2];
  int ret;
  ret = pipe(pipe0);
  ret = pipe(pipe1);
  printf("0\n");
  //if(fork()==0) 
    //startShell(pipe0[0], pipe1[1]);
  
  

  char buffer[1000];
  int nbytes;

  while(1)
  {
    printf("opening\n");
    int fd_in, fd_out;
    fd_in = open("/tmp/sh_in", O_RDONLY);
    fd_out = open("/tmp/sh_out", O_WRONLY);
    
    printf("read\n");
    nbytes=read(fd_in, buffer, 1000);
    write(pipe0[1], buffer, nbytes);
    
    nbytes=read(pipe1[0], buffer, 1000);
    write(fd_out, buffer, nbytes);
    
    close(fd_in);
    close(fd_out);
  }

}


int main(void)
{
  int o = mkfifo( "/tmp/sh_in", 0666 );
  o= mkfifo( "/tmp/sh_out", 0666);

  initbash();
  //int res = fork();
  //if(res==0) startbash();
  //wait(NULL);  
  return 0;
}

