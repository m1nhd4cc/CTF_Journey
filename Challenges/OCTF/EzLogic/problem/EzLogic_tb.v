`timescale 1us / 100ns

module EzLogic_tb #(
    parameter FLAG_TO_TEST = "..........................................",
    parameter N = 42
)();
    reg clk;
    reg rst_n;
    reg valid_in;
    reg start;
    reg [7:0] data_in;
    reg [6:0] counter;
    reg [6:0] counter2;
    wire [7:0] data_out;
    wire valid_out;
    reg [0:8*N-1] data_out_all;
    wire success;

    wire [7:0] flag_test_arr [0:N-1];
    genvar i;
    generate
        for (i=0;i<N;i=i+1) begin
            assign flag_test_arr[N-1-i] = FLAG_TO_TEST[(i*8)+:8];
        end
    endgenerate

    EzLogic_top inst(
        .clk(clk),
        .rst_n(rst_n),
        .data_in(data_in),
        .valid_in(valid_in),
        .data_out(data_out),
        .valid_out(valid_out)
    );

    initial begin
        $dumpfile("EzLogic_tb.vcd");
        $dumpvars(0, EzLogic_tb);
        clk = 0;
        rst_n = 0;
        data_in = 0;
        valid_in = 0;
        counter = 0;
        counter2 = 0;
        start = 0;
        data_out_all = 0;
        #4
        rst_n = 1;
        start = 1;
        @(negedge start);
        #4
        if (success) begin
            $display("Great! You've found the correct flag!");
        end
        else begin
            $display("Haha, try again!");
        end
        #20
        $finish();
    end

    always @(posedge clk) begin
        if (start == 1) begin
            if (counter < N) begin
                counter <= counter + 1;
                data_in <= flag_test_arr[counter];
                valid_in <= 1;
            end
            else begin
                data_in <= 0;
                valid_in <= 0;
                start <= 0;
            end
        end
    end

    always @(posedge clk) begin
        if (valid_out) begin
            counter2 <= counter2 + 1;
            data_out_all[(counter2)*8 +: 8] <= data_out;
        end
    end

    wire [0:8*N-1] data_std = 'h30789d5692f2fe23bb2c5d9e16406653b6cb217c952998ce17b7143788d949952680b4bce4c30a96c753;
    assign success = (data_std == data_out_all);

    always #1 clk = ~clk;
endmodule