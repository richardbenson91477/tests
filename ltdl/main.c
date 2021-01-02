#include <ltdl.h>
#include "c.h"

int main(void) {
    printf("begin main\n");

    lt_dlinit();

    lt_dlhandle _dl_c = lt_dlopen("./c.so");
    if (! _dl_c) {
        printf("lt_dlopen ./c.so failed\n");
        return -1;
    }

    NEW_C new_c = (NEW_C)lt_dlsym(_dl_c, "new_c");
    if (! new_c) { 
        printf("lt_dlsym failed: %s\n", lt_dlerror());
        return -2;
    }

    DEL_C del_c = (DEL_C)lt_dlsym(_dl_c, "del_c");
    if (! del_c) {
        printf("lt_dlsym failed: %s\n", lt_dlerror());
        return -3;
    }

    struct c *_c;
    new_c(&_c, 5);
    _c->print_x(_c);
    _c->x = 10;
    _c->print_x(_c);
    del_c(_c);

    lt_dlclose(_dl_c);
    lt_dlexit();

    printf("end main\n");
    return 0;
}

