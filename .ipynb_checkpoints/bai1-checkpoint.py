#!/usr/bin/env python
# coding: utf-8

# In[4]:


# #####################
# Cho phương trình hóa học: 3Fe +2O2 tạo thành Fe3O4. 
# Cho biết số mol của Fe là số A, số mol của O2 là B. 
# Yêu cầu: Hãy lập trình bằng python đưa ra phần nguyên số mol của chất sản phẩm Fe3O4. 
# Dữ liệu vào từ tệp văn bản HOAHOC.INP có 1 dòng duy nhất chứa hai số tự nhiên A và B. 
# Kết quả ghi ra tệp văn bản HOAHOC.OUT


# In[8]:


try:
    # Đọc dữ liệu từ tệp HOAHOC.INP
    with open('HOAHOC.INP', 'r') as file:
        data = file.readline().strip()
        values = data.split()
        
        if len(values) != 2:
            raise ValueError("Dữ liệu không đúng định dạng. Cần có 2 giá trị.")

        A, B = map(int, values)

    # Tính số mol của Fe3O4
    # Phương trình hóa học: 3Fe + 2O2 -> Fe3O4
    # Tỉ lệ mol: 3 mol Fe : 2 mol O2 -> 1 mol Fe3O4
    mol_Fe3O4 = min(A // 3, B // 2)

    # Ghi kết quả vào tệp HOAHOC.OUT
    with open('HOAHOC.OUT', 'w') as file:
        file.write(str(mol_Fe3O4))

except ValueError as e:
    print(f"Lỗi: {e}")


# In[ ]:




