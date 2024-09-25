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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumAquamarine
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(130, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(213, 30)
        self._label1.TabIndex = 0
        self._label1.Text = "length:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MediumAquamarine
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(130, 51)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(213, 27)
        self._label2.TabIndex = 1
        self._label2.Text = "width:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumAquamarine
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 136)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(213, 39)
        self._label3.TabIndex = 2
        self._label3.Text = "area:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MediumAquamarine
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 184)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(213, 39)
        self._label4.TabIndex = 3
        self._label4.Text = "perimeter:"
        self._label4.Click += self.Label4Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumTurquoise
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(349, 136)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(213, 39)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MediumTurquoise
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(349, 184)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(213, 39)
        self._label6.TabIndex = 5
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Cyan
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 265)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(100, 49)
        self._button1.TabIndex = 6
        self._button1.Text = "calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Cyan
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(232, 265)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(95, 49)
        self._button2.TabIndex = 7
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Cyan
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(465, 265)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(97, 49)
        self._button3.TabIndex = 8
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(349, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(213, 30)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(349, 48)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(213, 30)
        self._textBox2.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 0, 64)
        self.ClientSize = System.Drawing.Size(574, 326)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label4Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width = int(self._textBox2.Text)
        area = length * width
        perimeter = 2 * length + 2 * width
        self._label5.Text = str(area)
        self._label6.Text = str(perimeter)