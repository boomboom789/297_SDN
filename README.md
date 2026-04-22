# 297_SDN
Network utilisation Moniter 


📌 Problem Statement

Measure and display bandwidth utilization across the network.

---

## 🎯 Objectives

•⁠  ⁠Collect byte counters
•⁠  ⁠Estimate bandwidth usage
•⁠  ⁠Display used and unused bandwidth
•⁠  ⁠Update periodically

---

## 🧠 Technologies Used

•⁠  ⁠SDN (Software Defined Networking)
•⁠  ⁠POX Controller
•⁠  ⁠Mininet
•⁠  ⁠OpenFlow Protocol

---

## ⚙️ Setup / Execution Steps

### 1. Run POX Controller

⁠ bash
cd ~/pox
./pox.py monitor1 forwarding.l2_learning
 ⁠

### 2. Start Mininet

⁠ bash
sudo mn --topo single,3 --controller remote
 ⁠

### 3. Test Connectivity

⁠ bash
pingall
 ⁠

### 4. Generate Traffic

⁠ bash
h1 ping h2
 ⁠

### 5. High Traffic (iperf)

⁠ bash
h1 iperf -s &
h2 iperf -c h1
 ⁠

### 6. View Flow Table

⁠ bash
dpctl dump-flows
 ⁠

---

## 📊 Expected Output


===== NETWORK UTILIZATION =====
Total Bytes: 1200
Used Bandwidth (Bytes/sec): 240.0
Unused Bandwidth (Bytes/sec): 999760.0
Utilization (%): 0.024%


---

## 📸 Proof of Execution

•⁠  ⁠Controller running
•⁠  ⁠Mininet setup
•⁠  ⁠Ping results
•⁠  ⁠Iperf results
•⁠  ⁠Flow table entries
•⁠  ⁠Bandwidth utilization output
•⁠  ⁠No traffic case

---

## 🧪 Test Scenarios

### 1. Normal Case

•⁠  ⁠Ping works
•⁠  ⁠Bandwidth increases

### 2. No Traffic Case

•⁠  ⁠No packets
•⁠  ⁠Bandwidth = 0

---

## 📚 References

•⁠  ⁠https://mininet.org
•⁠  ⁠https://github.com/noxrepo/pox
•⁠  ⁠OpenFlow Documentation

---

## 👨‍💻 Author

Sushir C
