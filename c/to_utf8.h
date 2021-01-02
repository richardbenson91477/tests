static inline uint8_t to_utf8 (uint32_t ch, uint8_t *_b) {
    if (ch < 0x80) {
        _b[0] = ch;
        return 1;
    }
    else if (ch < 0x0800) {
        _b[0] = ((ch >> 6) & 0x1F) | 0xC0;
        _b[1] = (ch & 0x3F) | 0x80;
        return 2;
    }
    else if (ch < 0x010000) {
        _b[0] = ((ch >> 12) & 0x0F) | 0xE0;
        _b[1] = ((ch >> 6) & 0x3F) | 0x80;
        _b[2] = (ch & 0x3F) | 0x80;
        return 3;
    }
    else if (ch < 0x110000) {
        _b[0] = ((ch >> 18) & 0x07) | 0xF0;
        _b[1] = ((ch >> 12) & 0x3F) | 0x80;
        _b[2] = ((ch >> 6) & 0x3F) | 0x80;
        _b[3] = (ch & 0x3F) | 0x80;
        return 4;
    }
    else return 0;
}

