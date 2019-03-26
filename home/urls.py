"""aquaguard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import login,registration
# from .ProductViews import deleteDevice,getProductDetails
# from .adminViews import addNewLead, displayAssignedLeads, displaySingleLead, updateStatus,empLogin,getCallCount,setCallCount, loginPage, homePage, getSession

from .adminViews import *
from .EmployeeView import *
from .ServiceViews import *
from .ProductViews import *
from .CustomerViews import *

urlpatterns = [
    path("test/",Test),
    path("createNewEmployee/",createNewEmployee),
    # path("displayEmployee/",displayAllEmployee),
    # path("deactivateEmployee/",deactivateEmployee),
    # path("updateStatus/",updateStatus),
    # path("getCallCount/",getCallCount),
    # path("setCallCount/",setCallCount),
    path("editLead/", editLead),
    path("getSingleLead/", getSingleLead),
    # path("registerTicketExist/",existCustomerProblemRegistration),
    # path("registerTicket/",CustomerProblemRegistration),
    # path("checkPhone/",checkPhone),
    # path("checkMail/",checkMail),
    # path("addNewLead/",addNewLead),
    path("loginTechnician/", login),
    path("registerTechnician/", registration),
    # path("addNewProduct/", createNewDevice),
    # path("displayAllDevice/", displayAllDevice),
    # path("deleteDevice/", deleteDevice),
    path("changedp_tc/", changedp_tc),
    path("changedp_ad/", changedp_ad),
    path("getAssignedLeads/", getAssignedLeads), 
    path("getInterestedLeads/", getInterestedLeads),
    path("getLeadsNotContacted/", getLeadsNotContacted),
    path("getContactedLeads/", getContactedLeads),
    path("getUserData/", getUserData),
    path("getSession/", getSession),
    path("storeSession/", storeSession),
    path("flushSession/", flushSession),
    path("empLoginCheck/", empLoginCheck),
    path("storeLogoutTime/", storeLogoutTime),
    path("addProfilePic/", uploadEmployeeProfilePic),
    path("makeCall/", makeCall),
    path("getAllEmployees/", getAllEmployees),
    path("getAllActiveEmployees/", getAllActiveEmployees),
    path("addProfilePicture/", addProfilePicture),
    path("getProfilePicture/", getProfilePicture),
    path("setNotification/", setNotification),
    path("getNotification/", getNotification),
    path("setCommit/", setCommit),
    path("setPause/", togglePause),
    path("deleteSingleLead/", deleteSingleLead),
    path("setEmpTarget/", setEmpTarget),
    path("addNewProduct/", addNewProduct),
    path("getAllProducts/", getAllProducts),
    path("getSingleProduct/", getSingleProduct),
    path("updateProduct/", updateProduct),
    path("getEmpTarget/", getEmpTarget),
    path("getCallbackLeads/", getCallbackLeads),
    path("deleteMultipleLeads/", deleteMultipleLeads),
    path("addNewCustomer/", addNewCustomer),
    path("getSingleCustomer/", getSingleCustomer),
    path("getSingleEmployee/", getSingleEmployee),
    path("getAllUnAssignedLeads/", getAllUnAssignedLeads),
    path("assignLeads/", assignLeads),
    path("leadDataFileParser/", leadDataFileParser),
    #----------------------------------------------#
    path("", loginPage),

    path("obAdmin_tc_homePage/", obAdmin_tc_homePage),
    path("obAdmin_commitHistoryPage/", obAdmin_commitHistoryPage),
    path("obAdmin_callHistoryPage/", obAdmin_callHistoryPage),
    path("obAdmin_reportsPage/", obAdmin_reportsPage),
    
    path("tc_homePage/", tc_homePage),
    path("ad_homePage/", ad_homePage),
    path("homePageCommittedLeads/", homePageCommittedLeads),
    path("homePageContactLeads/", homePageContactLeads),
    path("callHistoryPage/", callHistoryPage),
    path("Edit_Remarks/",Edit_Remarks),
    path("commitHistoryPage/", commitHistoryPage),
    path("changedp_tc/", changedp_tc),
    path("adminStatistics/", adminStatistics),
    path("adminTask/", adminTask),
    path("Add_Leads/", Add_Leads),
    path("Assign_Leads/", Assign_Leads),
    path("Reassign_Leads/",Reassign_Leads),
    path("Lead_Status/",Lead_Status),
    path("assign_Employee/", assign_Employee),
    path("changedp_ad/", changedp_ad),
    path("forgotPassword/", forgotPassword),
    path("logoutPage/", logoutPage),
    path("remarks/", remarks),
    path("reportsPage/", reportsPage),
    path("mainEmployee/", mainEmployee),
    path("admin_tasks/", admin_tasks),
    path("assign_employee/", assign_employee),
    path("leads_delete/", leads_delete),

    #-------------changes by rahul -----------------#
    path("updateEmployee/", updateEmployee),
    # path("getProductDetail/",getProductDetails),

]
