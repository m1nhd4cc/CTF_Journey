// Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2020.2 (win64) Build 3064766 Wed Nov 18 09:12:45 MST 2020
// Date        : Sat Aug 31 17:14:12 2024
// Host        : DESKTOP-9V3OCBF running 64-bit major release  (build 9200)
// Command     : write_verilog -force EzLogic_top_synth.v
// Design      : EzLogic_top
// Purpose     : This is a Verilog netlist of the current design or from a specific cell of the design. The output is an
//               IEEE 1364-2001 compliant Verilog HDL file that contains netlist information obtained from the input
//               design files.
// Device      : xc7z010iclg225-1L
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* STRUCTURAL_NETLIST = "yes" *)
module EzLogic_top
   (clk,
    rst_n,
    data_in,
    valid_in,
    data_out,
    valid_out);
  input clk;
  input rst_n;
  input [7:0]data_in;
  input valid_in;
  output [7:0]data_out;
  output valid_out;

  wire \<const0> ;
  wire \<const1> ;
  wire clk;
  wire clk_IBUF;
  wire clk_IBUF_BUFG;
  wire [7:0]data_in;
  wire [7:0]data_in_IBUF;
  wire [7:0]data_out;
  wire [7:0]data_out_OBUF;
  wire \data_reg[3]_i_2_n_0 ;
  wire \data_reg[3]_i_3_n_0 ;
  wire \data_reg[3]_i_4_n_0 ;
  wire \data_reg[3]_i_5_n_0 ;
  wire \data_reg[7]_i_2_n_0 ;
  wire \data_reg[7]_i_3_n_0 ;
  wire \data_reg[7]_i_4_n_0 ;
  wire \data_reg[7]_i_5_n_0 ;
  wire \data_reg[7]_i_6_n_0 ;
  wire \data_reg_reg[3]_i_1_n_0 ;
  wire \data_reg_reg[3]_i_1_n_1 ;
  wire \data_reg_reg[3]_i_1_n_2 ;
  wire \data_reg_reg[3]_i_1_n_3 ;
  wire \data_reg_reg[7]_i_1_n_1 ;
  wire \data_reg_reg[7]_i_1_n_2 ;
  wire \data_reg_reg[7]_i_1_n_3 ;
  wire [7:0]p_0_in;
  wire rst_n;
  wire rst_n_IBUF;
  wire valid_in;
  wire valid_in_IBUF;
  wire valid_out;
  wire valid_out_OBUF;

  GND GND
       (.G(\<const0> ));
  VCC VCC
       (.P(\<const1> ));
  BUFG clk_IBUF_BUFG_inst
       (.I(clk_IBUF),
        .O(clk_IBUF_BUFG));
  IBUF clk_IBUF_inst
       (.I(clk),
        .O(clk_IBUF));
  IBUF \data_in_IBUF[0]_inst 
       (.I(data_in[0]),
        .O(data_in_IBUF[0]));
  IBUF \data_in_IBUF[1]_inst 
       (.I(data_in[1]),
        .O(data_in_IBUF[1]));
  IBUF \data_in_IBUF[2]_inst 
       (.I(data_in[2]),
        .O(data_in_IBUF[2]));
  IBUF \data_in_IBUF[3]_inst 
       (.I(data_in[3]),
        .O(data_in_IBUF[3]));
  IBUF \data_in_IBUF[4]_inst 
       (.I(data_in[4]),
        .O(data_in_IBUF[4]));
  IBUF \data_in_IBUF[5]_inst 
       (.I(data_in[5]),
        .O(data_in_IBUF[5]));
  IBUF \data_in_IBUF[6]_inst 
       (.I(data_in[6]),
        .O(data_in_IBUF[6]));
  IBUF \data_in_IBUF[7]_inst 
       (.I(data_in[7]),
        .O(data_in_IBUF[7]));
  OBUF \data_out_OBUF[0]_inst 
       (.I(data_out_OBUF[0]),
        .O(data_out[0]));
  OBUF \data_out_OBUF[1]_inst 
       (.I(data_out_OBUF[1]),
        .O(data_out[1]));
  OBUF \data_out_OBUF[2]_inst 
       (.I(data_out_OBUF[2]),
        .O(data_out[2]));
  OBUF \data_out_OBUF[3]_inst 
       (.I(data_out_OBUF[3]),
        .O(data_out[3]));
  OBUF \data_out_OBUF[4]_inst 
       (.I(data_out_OBUF[4]),
        .O(data_out[4]));
  OBUF \data_out_OBUF[5]_inst 
       (.I(data_out_OBUF[5]),
        .O(data_out[5]));
  OBUF \data_out_OBUF[6]_inst 
       (.I(data_out_OBUF[6]),
        .O(data_out[6]));
  OBUF \data_out_OBUF[7]_inst 
       (.I(data_out_OBUF[7]),
        .O(data_out[7]));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[3]_i_2 
       (.I0(data_out_OBUF[5]),
        .I1(data_in_IBUF[3]),
        .O(\data_reg[3]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[3]_i_3 
       (.I0(data_out_OBUF[6]),
        .I1(data_in_IBUF[2]),
        .O(\data_reg[3]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[3]_i_4 
       (.I0(data_out_OBUF[2]),
        .I1(data_in_IBUF[1]),
        .O(\data_reg[3]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[3]_i_5 
       (.I0(data_out_OBUF[4]),
        .I1(data_in_IBUF[0]),
        .O(\data_reg[3]_i_5_n_0 ));
  LUT1 #(
    .INIT(2'h1)) 
    \data_reg[7]_i_2 
       (.I0(rst_n_IBUF),
        .O(\data_reg[7]_i_2_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[7]_i_3 
       (.I0(data_out_OBUF[7]),
        .I1(data_in_IBUF[7]),
        .O(\data_reg[7]_i_3_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[7]_i_4 
       (.I0(data_out_OBUF[0]),
        .I1(data_in_IBUF[6]),
        .O(\data_reg[7]_i_4_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[7]_i_5 
       (.I0(data_out_OBUF[3]),
        .I1(data_in_IBUF[5]),
        .O(\data_reg[7]_i_5_n_0 ));
  LUT2 #(
    .INIT(4'h6)) 
    \data_reg[7]_i_6 
       (.I0(data_out_OBUF[1]),
        .I1(data_in_IBUF[4]),
        .O(\data_reg[7]_i_6_n_0 ));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[0] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[0]),
        .Q(data_out_OBUF[0]));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[1] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[1]),
        .Q(data_out_OBUF[1]));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[2] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[2]),
        .Q(data_out_OBUF[2]));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[3] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[3]),
        .Q(data_out_OBUF[3]));
  (* ADDER_THRESHOLD = "35" *) 
  CARRY4 \data_reg_reg[3]_i_1 
       (.CI(\<const0> ),
        .CO({\data_reg_reg[3]_i_1_n_0 ,\data_reg_reg[3]_i_1_n_1 ,\data_reg_reg[3]_i_1_n_2 ,\data_reg_reg[3]_i_1_n_3 }),
        .CYINIT(\<const0> ),
        .DI({data_out_OBUF[5],data_out_OBUF[6],data_out_OBUF[2],data_out_OBUF[4]}),
        .O(p_0_in[3:0]),
        .S({\data_reg[3]_i_2_n_0 ,\data_reg[3]_i_3_n_0 ,\data_reg[3]_i_4_n_0 ,\data_reg[3]_i_5_n_0 }));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[4] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[4]),
        .Q(data_out_OBUF[4]));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[5] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[5]),
        .Q(data_out_OBUF[5]));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[6] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[6]),
        .Q(data_out_OBUF[6]));
  FDCE #(
    .INIT(1'b0)) 
    \data_reg_reg[7] 
       (.C(clk_IBUF_BUFG),
        .CE(valid_in_IBUF),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(p_0_in[7]),
        .Q(data_out_OBUF[7]));
  (* ADDER_THRESHOLD = "35" *) 
  CARRY4 \data_reg_reg[7]_i_1 
       (.CI(\data_reg_reg[3]_i_1_n_0 ),
        .CO({\data_reg_reg[7]_i_1_n_1 ,\data_reg_reg[7]_i_1_n_2 ,\data_reg_reg[7]_i_1_n_3 }),
        .CYINIT(\<const0> ),
        .DI({\<const0> ,data_out_OBUF[0],data_out_OBUF[3],data_out_OBUF[1]}),
        .O(p_0_in[7:4]),
        .S({\data_reg[7]_i_3_n_0 ,\data_reg[7]_i_4_n_0 ,\data_reg[7]_i_5_n_0 ,\data_reg[7]_i_6_n_0 }));
  IBUF rst_n_IBUF_inst
       (.I(rst_n),
        .O(rst_n_IBUF));
  IBUF valid_in_IBUF_inst
       (.I(valid_in),
        .O(valid_in_IBUF));
  OBUF valid_out_OBUF_inst
       (.I(valid_out_OBUF),
        .O(valid_out));
  FDCE #(
    .INIT(1'b0)) 
    valid_out_reg
       (.C(clk_IBUF_BUFG),
        .CE(\<const1> ),
        .CLR(\data_reg[7]_i_2_n_0 ),
        .D(valid_in_IBUF),
        .Q(valid_out_OBUF));
endmodule
