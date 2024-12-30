<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Dashboard.aspx.cs" Inherits="" %>

<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head runat="server">
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <title>Material Dashboard 2</title>
    <link href="../assets/css/nucleo-icons.css" rel="stylesheet" />
    <link href="../assets/css/material-dashboard.css?v=3.0.0" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
    <style>
        .navbar-expand-xs.fixed-start {
            right: 0;
        }
    </style>
</head>
<body class="g-sidenav-show bg-gray-200">
    <form id="form1" runat="server">
        <aside class="sidenav navbar navbar-vertical navbar-expand-xs border-0 border-radius-xl my-3 fixed-start bg-gradient-dark">
            <div class="sidenav-header">
                <a class="navbar-brand m-0">
                    <img src="../assets/img/logo-ct.png" class="navbar-brand-img h-100" alt="main_logo" />
                    <span class="ms-1 font-weight-bold text-white">Material Dashboard 2</span>
                </a>
            </div>
            <hr class="horizontal light mt-0 mb-2" />
            <div class="collapse navbar-collapse w-auto max-height-vh-100">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link text-white" href="Dashboard.aspx">
                            <i class="material-icons opacity-10">dashboard</i>
                            <span class="nav-link-text ms-1">Dashboard</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white active bg-gradient-primary" href="Tables.aspx">
                            <i class="material-icons opacity-10">table_view</i>
                            <span class="nav-link-text ms-1">Tables</span>
                        </a>
                    </li>
                </ul>
            </div>
        </aside>

        <main class="main-content position-relative max-height-vh-100 h-100 border-radius-lg mt-4">
            <div class="container-fluid py-4">
                <div class="row">
                    <div class="col-12">
                        <div class="card my-4">
                            <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
                                <div class="bg-gradient-primary shadow-primary border-radius-lg pt-4 pb-3">
                                    <h6 class="text-white text-capitalize ps-3">تقرير الفواتير</h6>
                                </div>
                            </div>
                            <div class="card-body px-0 pb-2">
                                <asp:GridView ID="GridView1" runat="server" CssClass="table align-items-center mb-0">
                                    <Columns>
                                        <asp:BoundField DataField="InvoiceNumber" HeaderText="رقم الفاتورة" />
                                        <asp:BoundField DataField="Date" HeaderText="التاريخ" />
                                        <asp:BoundField DataField="Customer" HeaderText="العميل" />
                                        <asp:BoundField DataField="Value" HeaderText="القيمة" />
                                        <asp:BoundField DataField="Tax" HeaderText="الضريبة" />
                                        <asp:BoundField DataField="Total" HeaderText="الإجمالي" />
                                        <asp:BoundField DataField="Reference" HeaderText="المرجع" />
                                        <asp:BoundField DataField="Notes" HeaderText="الملاحظات" />
                                    </Columns>
                                </asp:GridView>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </form>
</body>
</html>
