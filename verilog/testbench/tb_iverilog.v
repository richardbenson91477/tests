
module test;

reg clk = 0;
always #1 clk=~clk;

reg [31:0] cnt = 0;

initial
begin
//      $dumpfile("your_choice_of_name.vcd");
//      $dumpvars;
    $display("init");
end

always @(posedge clk)
begin
    cnt <= cnt + 1;
    if (cnt == 10000) begin
        cnt <= 0;
        $display("cnt = ", cnt);
    end

//    $stop;
//    $finish;
end

endmodule

