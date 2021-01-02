module led2 (
    input CLK,
    input PIN_14,
    output LED,
    output USBPU
    );

assign USBPU = 0;

reg [24:0] c;

always @(posedge CLK) begin
   c <= c + !PIN_14;
end

assign LED = c[24];

endmodule

