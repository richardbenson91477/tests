
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <jni.h>

void Java_jni1_foo (JNIEnv *env, jobject obj) {
    printf ("Java_jni1_foo ()\n");
}

