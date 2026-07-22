FORMULAS = {

"Basic Electrical Engineering": {

"Ohm's Law": "V = IR",

"Current Formula": "I = V/R",

"Resistance Formula": "R = V/I",

"Electrical Power": "P = VI",

"Power using Current": "P = I²R",

"Power using Voltage": "P = V²/R",

"Electrical Energy": "E = Pt",

"Charge": "Q = It",

"Resistance": "R = ρL/A",

"Conductance": "G = 1/R",

"Conductivity": "σ = 1/ρ",

"Current Density": "J = I/A",

"Electric Field": "E = F/Q",

"Potential Difference": "V = W/Q",

"Capacitance": "C = Q/V",

"Capacitor Energy": "E = ½CV²",

"Capacitive Reactance": "XC = 1/(2πfC)",

"Inductive Reactance": "XL = 2πfL",

"Inductance Voltage": "V = L(di/dt)",

"Capacitor Current": "I = C(dv/dt)",

"Kirchhoff Current Law": "ΣI = 0",

"Kirchhoff Voltage Law": "ΣV = 0",

"Series Resistance": "R = R1 + R2 + R3",

"Parallel Resistance": "1/R = 1/R1 + 1/R2 + 1/R3",

"Maximum Power Transfer": "RL = RTH"

},



"Network Theory": {

"Mesh Equation": "ΣV = 0",

"Nodal Equation": "ΣI = 0",

"Thevenin Voltage": "VTH = VOC",

"Thevenin Resistance": "RTH = VOC/ISC",

"Norton Current": "IN = ISC",

"Norton Resistance": "RN = RTH",

"Source Transformation": "V = IR",

"Superposition Principle": "Total Response = Sum of Individual Responses",

"Millman's Theorem": "V = Σ(GV)/ΣG",

"Reciprocity Theorem": "Transfer Ratio is Same",

"Compensation Theorem": "ΔI = ΔV/R",

"Maximum Power": "Pmax = V²/4R",

"Star to Delta": "RAB=(R1R2+R2R3+R3R1)/R3",

"Delta to Star": "RA=(RAB×RCA)/(RAB+RBC+RCA)",

"Time Constant RC": "τ = RC",

"Time Constant RL": "τ = L/R",

"Transient Current": "I = Imax(1-e^(-t/τ))",

"Transient Voltage": "V = Vmax(1-e^(-t/τ))",

"Steady State": "di/dt = 0",

"Natural Response": "Ae^(-t/τ)"

},



"AC Circuits": {

"RMS Voltage": "Vrms = Vm/√2",

"RMS Current": "Irms = Im/√2",

"Average Voltage": "Vavg = 2Vm/π",

"Average Current": "Iavg = 2Im/π",

"Angular Frequency": "ω = 2πf",

"Frequency": "f = 1/T",

"Time Period": "T = 1/f",

"Inductive Reactance": "XL = ωL",

"Capacitive Reactance": "XC = 1/ωC",

"Impedance": "Z = R + jX",

"Impedance Magnitude": "Z = √(R²+X²)",

"Phase Angle": "φ = tan⁻¹(X/R)",

"Power Factor": "cosφ = P/S",

"Real Power": "P = VIcosφ",

"Reactive Power": "Q = VIsinφ",

"Apparent Power": "S = VI",

"Complex Power": "S = P + jQ",

"Resonant Frequency": "fr = 1/(2π√LC)",

"Quality Factor": "Q = XL/R",

"Bandwidth": "BW = fr/Q"

},

 #Basic Electrical Engineering → 25 formulas
 #Network Theory → 20 formulas
#AC Circuits → 20 formulas


"Electrical Machines": {

"Transformer EMF Equation": "E = 4.44fNΦm",

"Transformer Turns Ratio": "V₁/V₂ = N₁/N₂",

"Transformer Current Ratio": "I₁/I₂ = N₂/N₁",

"Transformer Efficiency": "η = (Output/Input) × 100",

"Voltage Regulation": "%VR = ((VNL - VFL)/VFL) × 100",

"Copper Loss": "Pc = I²R",

"Iron Loss": "Pi = Ph + Pe",

"Hysteresis Loss": "Ph = KhfBm^1.6",

"Eddy Current Loss": "Pe = Kef²Bm²t²",

"Transformer Output": "P = VIcosφ",

"DC Generator EMF": "Eg = (PΦZN)/(60A)",

"Back EMF": "Eb = V - IaRa",

"DC Motor Speed": "N ∝ (V - IaRa)/Φ",

"Torque Equation": "T = 9.55P/N",

"Electrical Torque": "T = P/ω",

"Mechanical Power": "Pm = Tω",

"Synchronous Speed": "Ns = (120f)/P",

"Slip": "s = (Ns - N)/Ns",

"Slip Percentage": "%Slip = ((Ns - N)/Ns) × 100",

"Rotor Frequency": "fr = sf",

"Rotor EMF": "Er = sE₂",

"Rotor Reactance": "Xr = sX₂",

"Induction Motor Torque": "T ∝ (sR₂)/(R₂² + (sX₂)²)",

"Maximum Torque Slip": "sm = R₂/X₂",

"Mechanical Speed": "N = (1 - s)Ns",

"Rotor Copper Loss": "Rotor Loss = sPg",

"Mechanical Power Developed": "Pm = (1 - s)Pg",

"Synchronous Motor Power": "P = (EV/Xs) sinδ",

"Synchronous Motor Torque": "T = P/ω",

"Motor Efficiency": "η = (Output/Input) × 100"

},


"Power Systems": {

"Single Phase Power": "P = VIcosφ",

"Reactive Power": "Q = VIsinφ",

"Apparent Power": "S = VI",

"Three Phase Active Power": "P = √3 VLILcosφ",

"Three Phase Reactive Power": "Q = √3 VLILsinφ",

"Three Phase Apparent Power": "S = √3 VLIL",

"Power Factor": "cosφ = P/S",

"Power Factor Angle": "φ = cos⁻¹(P/S)",

"Line Voltage (Star)": "VL = √3 VPH",

"Line Current (Star)": "IL = IPH",

"Line Voltage (Delta)": "VL = VPH",

"Line Current (Delta)": "IL = √3 IPH",

"Transmission Efficiency": "η = (PR/PS) × 100",

"Voltage Regulation": "%VR = ((VS - VR)/VR) × 100",

"Transmission Loss": "Ploss = I²R",

"Short Circuit Current": "Isc = V/Z",

"Fault Current": "If = V/Zf",

"Per Unit Value": "PU = Actual/Base",

"Base Current": "Ib = Sb/(√3 Vb)",

"Base Impedance": "Zb = Vb²/Sb",

"Base Power": "Sb = √3 VLIL",

"Load Factor": "Average Load / Maximum Demand",

"Demand Factor": "Maximum Demand / Connected Load",

"Diversity Factor": "Sum of Individual Maximum Demands / Maximum Demand",

"Capacity Factor": "Average Load / Plant Capacity",

"Plant Use Factor": "Energy Generated / (Plant Capacity × Hours)",

"Utilization Factor": "Maximum Demand / Plant Capacity",

"Load Diversity": "Σ Individual Loads / Maximum Demand",

"Receiving End Power": "PR = VRIRcosφ",

"Sending End Power": "PS = VSIScosφ",

"Voltage Drop": "ΔV = IR",

"Charging Current": "Ic = V/Xc",

"Surge Impedance": "Z0 = √(L/C)",

"Surge Impedance Loading": "SIL = VL²/Z0",

"Corona Loss": "Pc = 241(f+25)(V-Vd)²√(r/d)"

},


"Power Electronics": {

"Average Output Voltage (Half Wave Rectifier)": "Vdc = Vm/π",

"RMS Output Voltage (Half Wave Rectifier)": "Vrms = Vm/2",

"Average Output Voltage (Full Wave Rectifier)": "Vdc = 2Vm/π",

"RMS Output Voltage (Full Wave Rectifier)": "Vrms = Vm/√2",

"Ripple Factor (Half Wave)": "r = 1.21",

"Ripple Factor (Full Wave)": "r = 0.482",

"Rectifier Efficiency (Half Wave)": "η = 40.6%",

"Rectifier Efficiency (Full Wave)": "η = 81.2%",

"Peak Inverse Voltage (Half Wave)": "PIV = Vm",

"Peak Inverse Voltage (Full Wave Center Tap)": "PIV = 2Vm",

"Peak Inverse Voltage (Bridge Rectifier)": "PIV = Vm",

"Ripple Voltage": "Vr = √(Vrms² - Vdc²)",

"Ripple Factor": "r = Vr/Vdc",

"Form Factor": "FF = Vrms/Vdc",

"Transformer Utilization Factor": "TUF = Pdc/Transformer Rating",

"SCR Average Current": "Iavg = Vdc/RL",

"SCR RMS Current": "Irms = Vrms/RL",

"Firing Angle": "α",

"Conduction Angle": "β = π - α",

"Duty Cycle": "D = Ton/T",

"Buck Converter Output": "Vo = DVs",

"Boost Converter Output": "Vo = Vs/(1-D)",

"Buck Boost Converter": "Vo = -DVs/(1-D)",

"Cuk Converter": "Vo = -DVs/(1-D)",

"SEPIC Converter": "Vo = DVs/(1-D)",

"Flyback Converter": "Vo = (Ns/Np)(D/(1-D))Vs",

"Forward Converter": "Vo = (Ns/Np)DVs",

"Switching Frequency": "f = 1/T",

"Switching Period": "T = 1/f",

"PWM Frequency": "fPWM = 1/T",

"Output Power": "Po = VoIo",

"Input Power": "Pin = VsIs",

"Converter Efficiency": "η = Po/Pin ×100",

"Inductor Energy": "E = ½LI²",

"Capacitor Energy": "E = ½CV²"

}
}