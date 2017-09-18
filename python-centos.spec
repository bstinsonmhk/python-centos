%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		python-centos
Version:	0.1.1
Release:	2%{?dist}
Summary:	Python bindings for the CentOS account system, CBS and other services

Group:		Applications/System
License:	GPLv2
URL:		https://github.com/bstinsonmhk/python-centos
Source0:	python-centos-%{version}.tar.gz

BuildRequires:	python-devel, python-setuptools
Requires:   pyOpenSSL
Requires:   python-munch
Requires:   python-requests
Requires:   python-urllib3
Requires:   python-lockfile
Requires:   python-kitchen

BuildArch: noarch

%description
Provides python bindings for the infrastructure services in the CentOS project

%prep
%setup -q -c -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%{python_sitelib}/*

%changelog
* Wed Jul 19 2017 brian@bstinson.com 0.1.1-2
- Bumpspec to rebuild for F26

* Tue Jul 05 2016 brian@bstinson.com 0.1.1-1
- Fix CentOSUserCert to verify as false if the cert is expired

* Tue Nov 10 2015 brian@bstinson.com 0.1.0-2
- Adding a hard dep on python-kitchen

* Wed Oct 28 2015 brian@bstinson.com 0.1.0-1
- Update to point to the prod location of FAS

* Thu Sep 03 2015 brian@bstinson.com 0.0.4-1
- Add the AccountSystem and a BR for python-fedora

* Tue Aug 11 2015 brian@bstinson.com 0.0.2-1
- Updated to dev version of library defaults 

* Sun Jul 26 2015 brian@bstinson.com 0.0.1-1
- First build


