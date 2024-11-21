import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label3 = System.Windows.Forms.Label()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label9 = System.Windows.Forms.Label()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label10 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label20 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._label19 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label21 = System.Windows.Forms.Label()
        self._label22 = System.Windows.Forms.Label()
        self._label23 = System.Windows.Forms.Label()
        self._label24 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Maroon
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Agency FB", 26, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label1.Location = System.Drawing.Point(100, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(213, 56)
        self._label1.TabIndex = 0
        self._label1.Text = "Highlander Hotel"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Maroon
        self._label2.Font = System.Drawing.Font("Agency FB", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label2.Location = System.Drawing.Point(100, 73)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(108, 36)
        self._label2.TabIndex = 1
        self._label2.Text = "Today's Date:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # groupBox1
        # 
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._label6)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 148)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(190, 113)
        self._groupBox1.TabIndex = 2
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Room Information"
        self._groupBox1.Enter += self.GroupBox1Enter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Maroon
        self._label3.Font = System.Drawing.Font("Agency FB", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label3.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label3.Location = System.Drawing.Point(100, 109)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(108, 36)
        self._label3.TabIndex = 3
        self._label3.Text = "Time:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # groupBox2
        # 
        self._groupBox2.Controls.Add(self._label10)
        self._groupBox2.Controls.Add(self._textBox5)
        self._groupBox2.Controls.Add(self._label9)
        self._groupBox2.Controls.Add(self._textBox4)
        self._groupBox2.Controls.Add(self._label8)
        self._groupBox2.Controls.Add(self._textBox3)
        self._groupBox2.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._groupBox2.Location = System.Drawing.Point(220, 148)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(190, 113)
        self._groupBox2.TabIndex = 3
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Additional Charges"
        # 
        # groupBox3
        # 
        self._groupBox3.Controls.Add(self._label24)
        self._groupBox3.Controls.Add(self._label22)
        self._groupBox3.Controls.Add(self._label23)
        self._groupBox3.Controls.Add(self._label21)
        self._groupBox3.Controls.Add(self._label20)
        self._groupBox3.Controls.Add(self._label15)
        self._groupBox3.Controls.Add(self._label14)
        self._groupBox3.Controls.Add(self._label11)
        self._groupBox3.Controls.Add(self._label12)
        self._groupBox3.Controls.Add(self._label13)
        self._groupBox3.Font = System.Drawing.Font("Agency FB", 17, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._groupBox3.Location = System.Drawing.Point(12, 267)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(398, 183)
        self._groupBox3.TabIndex = 4
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Additional Charges"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.IndianRed
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(84, 38)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.IndianRed
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(84, 72)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 20)
        self._textBox2.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Snow
        self._button1.FlatAppearance.BorderColor = System.Drawing.Color.Red
        self._button1.FlatAppearance.BorderSize = 0
        self._button1.Font = System.Drawing.Font("Agency FB", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._button1.Location = System.Drawing.Point(27, 456)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(125, 40)
        self._button1.TabIndex = 7
        self._button1.Text = "Calculate Charges"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Snow
        self._button2.FlatAppearance.BorderColor = System.Drawing.Color.Red
        self._button2.FlatAppearance.BorderSize = 0
        self._button2.Font = System.Drawing.Font("Agency FB", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._button2.Location = System.Drawing.Point(158, 456)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(114, 40)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Snow
        self._button3.FlatAppearance.BorderColor = System.Drawing.Color.Red
        self._button3.FlatAppearance.BorderSize = 0
        self._button3.Font = System.Drawing.Font("Agency FB", 13, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._button3.Location = System.Drawing.Point(278, 456)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(116, 40)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Maroon
        self._label4.Font = System.Drawing.Font("Agency FB", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label4.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label4.Location = System.Drawing.Point(214, 83)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(205, 20)
        self._label4.TabIndex = 10
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Maroon
        self._label5.Font = System.Drawing.Font("Agency FB", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label5.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label5.Location = System.Drawing.Point(214, 119)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(205, 20)
        self._label5.TabIndex = 11
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Maroon
        self._label6.Font = System.Drawing.Font("Agency FB", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label6.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label6.Location = System.Drawing.Point(15, 34)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(67, 26)
        self._label6.TabIndex = 12
        self._label6.Text = "Nights:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Maroon
        self._label7.Font = System.Drawing.Font("Agency FB", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label7.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label7.Location = System.Drawing.Point(6, 69)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(76, 26)
        self._label7.TabIndex = 13
        self._label7.Text = "Nightly Charge:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Maroon
        self._label8.Font = System.Drawing.Font("Agency FB", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label8.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label8.Location = System.Drawing.Point(6, 29)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(76, 26)
        self._label8.TabIndex = 15
        self._label8.Text = "Room Service:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox3
        # 
        self._textBox3.BackColor = System.Drawing.Color.IndianRed
        self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(84, 32)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 20)
        self._textBox3.TabIndex = 14
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.Maroon
        self._label9.Font = System.Drawing.Font("Agency FB", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label9.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label9.Location = System.Drawing.Point(6, 55)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(76, 26)
        self._label9.TabIndex = 17
        self._label9.Text = "Telephone:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox4
        # 
        self._textBox4.BackColor = System.Drawing.Color.IndianRed
        self._textBox4.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(84, 58)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 20)
        self._textBox4.TabIndex = 16
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.Maroon
        self._label10.Font = System.Drawing.Font("Agency FB", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label10.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label10.Location = System.Drawing.Point(6, 81)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(76, 26)
        self._label10.TabIndex = 19
        self._label10.Text = "Misc:"
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox5
        # 
        self._textBox5.BackColor = System.Drawing.Color.IndianRed
        self._textBox5.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 13, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(84, 84)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 20)
        self._textBox5.TabIndex = 18
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.Maroon
        self._label11.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label11.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label11.Location = System.Drawing.Point(50, 90)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(146, 26)
        self._label11.TabIndex = 22
        self._label11.Text = "Subtotal:"
        self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.Maroon
        self._label12.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label12.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label12.Location = System.Drawing.Point(50, 60)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(146, 26)
        self._label12.TabIndex = 21
        self._label12.Text = "Additional Charges:"
        self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.Maroon
        self._label13.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label13.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label13.Location = System.Drawing.Point(50, 30)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(146, 26)
        self._label13.TabIndex = 20
        self._label13.Text = "Room Charges:"
        self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.Maroon
        self._label14.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label14.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label14.Location = System.Drawing.Point(50, 120)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(146, 26)
        self._label14.TabIndex = 23
        self._label14.Text = "Tax:"
        self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.Maroon
        self._label15.Font = System.Drawing.Font("Agency FB", 16, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label15.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label15.Location = System.Drawing.Point(50, 150)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(146, 26)
        self._label15.TabIndex = 24
        self._label15.Text = "Total Charges:"
        self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label20
        # 
        self._label20.BackColor = System.Drawing.Color.Maroon
        self._label20.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label20.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label20.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label20.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label20.Location = System.Drawing.Point(194, 30)
        self._label20.Name = "label20"
        self._label20.Size = System.Drawing.Size(122, 27)
        self._label20.TabIndex = 25
        self._label20.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.IndianRed
        self._label17.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label17.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._label17.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label17.Location = System.Drawing.Point(202, 110)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(122, 26)
        self._label17.TabIndex = 28
        self._label17.Text = "Tax:"
        self._label17.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.IndianRed
        self._label18.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label18.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._label18.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label18.Location = System.Drawing.Point(202, 84)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(122, 26)
        self._label18.TabIndex = 27
        self._label18.Text = "Subtotal:"
        self._label18.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label19
        # 
        self._label19.BackColor = System.Drawing.Color.IndianRed
        self._label19.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label19.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._label19.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label19.Location = System.Drawing.Point(202, 58)
        self._label19.Name = "label19"
        self._label19.Size = System.Drawing.Size(122, 26)
        self._label19.TabIndex = 26
        self._label19.Text = "Additional Charges:"
        self._label19.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.IndianRed
        self._label16.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label16.ForeColor = System.Drawing.Color.FromArgb(64, 0, 0)
        self._label16.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label16.Location = System.Drawing.Point(202, 136)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(122, 26)
        self._label16.TabIndex = 29
        self._label16.Text = "Total Charges:"
        self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label21
        # 
        self._label21.BackColor = System.Drawing.Color.Maroon
        self._label21.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label21.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label21.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label21.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label21.Location = System.Drawing.Point(194, 60)
        self._label21.Name = "label21"
        self._label21.Size = System.Drawing.Size(122, 27)
        self._label21.TabIndex = 26
        self._label21.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label22
        # 
        self._label22.BackColor = System.Drawing.Color.Maroon
        self._label22.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label22.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label22.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label22.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label22.Location = System.Drawing.Point(194, 120)
        self._label22.Name = "label22"
        self._label22.Size = System.Drawing.Size(122, 27)
        self._label22.TabIndex = 28
        self._label22.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label23
        # 
        self._label23.BackColor = System.Drawing.Color.Maroon
        self._label23.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label23.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label23.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label23.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label23.Location = System.Drawing.Point(194, 90)
        self._label23.Name = "label23"
        self._label23.Size = System.Drawing.Size(122, 27)
        self._label23.TabIndex = 27
        self._label23.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label24
        # 
        self._label24.BackColor = System.Drawing.Color.Maroon
        self._label24.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label24.Font = System.Drawing.Font("Agency FB", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label24.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label24.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label24.Location = System.Drawing.Point(194, 150)
        self._label24.Name = "label24"
        self._label24.Size = System.Drawing.Size(122, 27)
        self._label24.TabIndex = 29
        self._label24.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(422, 504)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pg162RoomCharge"
        self.Load += self.MainFormLoad
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self._groupBox2.ResumeLayout(False)
        self._groupBox2.PerformLayout()
        self._groupBox3.ResumeLayout(False)
        self.ResumeLayout(False)


    def GroupBox1Enter(self, sender, e):
        pass

    def MainFormLoad(self, sender, e):
        from datetime import date 
        self._label4.Text = date.today().strftime("%A, %B %d, %Y")
        import time 
        self._label5.Text = time.strftime("%I:%M:%S %p")

    def Button1Click(self, sender, e):
        decRoomCharges = 0.0
        decAddCharges  = 0.0
        decSubtotal    = 0.0
        decTotal       = 0.0
        decTAX_RATE    = 0.08
        
        try: 
            decAddCharges = float(self._textBox3.Text) + \
                float(self._textBox4.Text) + \
                float(self._textBox5.Text)
            self._label21.Text = str(round(decAddCharges, 2))
        except:
            MessageBox.Show("Room Servie, Telephone, and Misc. must be numbers", "Error")
        
        try:
            decRoomCharges = float(self._textBox1.Text) * \
                float(self._textBox2.Text)
            self._label20.Text = str(round(decRoomCharges, 2))
        except:
            MessageBox.Show("Nights and Nightly Charge must be numbers", "Error")