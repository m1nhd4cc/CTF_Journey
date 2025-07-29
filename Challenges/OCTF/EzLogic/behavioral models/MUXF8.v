`ifdef verilator3
`else
`timescale 1 ps / 1 ps
`endif

/* verilator coverage_off */
module MUXF8
(
    input  wire I0, I1, S,
    output wire O
);
    wire [1:0] w_data = { I1, I0 };

    assign O = w_data[S];

endmodule
/* verilator coverage_on */
