import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Thistle
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(173, 9)
        self._textBox1.Multiline = True
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 23)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Thistle
        self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(173, 36)
        self._textBox2.Multiline = True
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 23)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Lavender
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Navy
        self._label1.Location = System.Drawing.Point(173, 73)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 2
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Lavender
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.Color.Navy
        self._label2.Location = System.Drawing.Point(173, 105)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 3
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Lavender
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.Color.Navy
        self._label3.Location = System.Drawing.Point(173, 135)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 4
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Thistle
        self._label4.Font = System.Drawing.Font("Berlin Sans FB Demi", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.Color.DarkMagenta
        self._label4.Location = System.Drawing.Point(17, 9)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(156, 23)
        self._label4.TabIndex = 5
        self._label4.Text = "Sales for the month:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Thistle
        self._label5.Font = System.Drawing.Font("Berlin Sans FB Demi", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.DarkMagenta
        self._label5.Location = System.Drawing.Point(17, 36)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(156, 23)
        self._label5.TabIndex = 6
        self._label5.Text = "Advance pay awarded:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Lavender
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label6.Font = System.Drawing.Font("Berlin Sans FB Demi", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.DarkMagenta
        self._label6.Location = System.Drawing.Point(53, 73)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(115, 23)
        self._label6.TabIndex = 7
        self._label6.Text = "Comission rate:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Lavender
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label7.Font = System.Drawing.Font("Berlin Sans FB Demi", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.Color.DarkMagenta
        self._label7.Location = System.Drawing.Point(53, 105)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(115, 23)
        self._label7.TabIndex = 8
        self._label7.Text = "Commissions:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Lavender
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        self._label8.Font = System.Drawing.Font("Berlin Sans FB Demi", 10, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.Color.DarkMagenta
        self._label8.Location = System.Drawing.Point(53, 135)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(115, 23)
        self._label8.TabIndex = 9
        self._label8.Text = "Net pay:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Gadugi", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.DimGray
        self._button1.Location = System.Drawing.Point(27, 167)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 25)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Gadugi", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.DimGray
        self._button2.Location = System.Drawing.Point(108, 167)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(75, 25)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button3.Font = System.Drawing.Font("Gadugi", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Maroon
        self._button3.Location = System.Drawing.Point(189, 167)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(75, 25)
        self._button3.TabIndex = 12
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.AliceBlue
        self.ClientSize = System.Drawing.Size(292, 204)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Pg240Comm"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._label2.Text = ""
        self._label3.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button1Click(self, sender, e):
        try:
            sales = float(self._textBox1.Text)
        except:
            MessageBox.Show("Please enter a sales amount.", "Error")
            return
        try:
            advance = float(self._textBox2.Text)
        except:
            MessageBox.Show("Please enter an advance amount.", "Error")
            return
        
        if sales < 10000:
            rate = .05
        elif sales >= 10000 and sales <= 14999:
            rate = .1
        elif sales >= 15000 and sales <= 17999:
            rate = .12
        elif sales >= 18000 and sales <= 21999:
            rate = .14
        else:
            rate = .16
        
        commission = sales * rate
        net = commission - advance
        
            
        self._label1.Text = "12.00%"
        self._label2.Text = "$" + str(round(commission, 2))
        self._label3.Text = "$" + str(round(net, 2))