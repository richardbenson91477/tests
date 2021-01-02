module led1 (
    input CLK,
    output LED,
    output USBPU
    );

assign USBPU = 0;

reg [24:0] c;

always @(posedge CLK) begin
    c <= c + 1;
end

assign LED = c[24];

endmodule

