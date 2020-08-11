%global srcname     centos
%global common_description %{expand:
Provides python bindings for the infrastructure services in the CentOS project.}

# Enable/disable building against specific Pythons
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
# On Fedora and newer EL: build only Python3 by default
%bcond_with         python2
%bcond_without      python3
# In this setup, there are automatic dependency generators available
%global             has_dependency_generators   1
%else
# On older Fedora and EL: build both Python 2 and 3 by default
%bcond_without      python2
%bcond_without      python3
# In this setup, automatic dependency generators are not available
%global             has_dependency_generators   0
%endif

# Specifically on EPEL, enable building against another Python 3
%{?epel:%bcond_without python3_other}

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:       python-%{srcname}
Version:    0.2.0
Release:    1%{?dist}
Summary:    Python bindings for the CentOS account system, CBS and other services

Group:      Applications/System
License:    GPLv2
URL:        https://centos.org/
Source0:    python-centos-%{version}.tar.gz

BuildArch:  noarch

%description %{common_description}

%if %{has_dependency_generators}
%{?python_enable_dependency_generator}
%endif

%if %{with python2}
%global py2_pkgname     %{expand:python2-%{srcname}}

%package -n %{py2_pkgname}
Summary:    %{summary}
%{?python_provide:%python_provide %{py2_pkgname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%if !%{has_dependency_generators}
# On older releases, unversioned python is Python 2
Requires:       pyOpenSSL
Requires:       python-kitchen
Requires:       python-lockfile
Requires:       python-munch
Requires:       python-requests
Requires:       python-urllib3
%endif

%description -n %{py2_pkgname} %{common_description}
%endif

%if %{with python3}
%global py3_pkgname     %{expand:python%{python3_pkgversion}-%{srcname}}

%package -n %{py3_pkgname}
Summary:    %{summary}
%{?python_provide:%python_provide %{py3_pkgname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if !%{has_dependency_generators}
Requires:       python%{python3_pkgversion}-pyOpenSSL
Requires:       python%{python3_pkgversion}-kitchen
Requires:       python%{python3_pkgversion}-lockfile
Requires:       python%{python3_pkgversion}-munch
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-urllib3
%endif

%description -n %{py3_pkgname} %{common_description}
%endif

%if %{with python3_other}
%global py3_other_pkgname %{expand:python%{python3_other_pkgversion}-%{srcname}}

%package -n %{py3_other_pkgname}
Summary:    %{summary}
%{?python_provide:%python_provide %{py3_other_pkgname}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools

%if !%{has_dependency_generators}
Requires:       python%{python3_other_pkgversion}-pyOpenSSL
Requires:       python%{python3_other_pkgversion}-kitchen
Requires:       python%{python3_other_pkgversion}-lockfile
Requires:       python%{python3_other_pkgversion}-munch
Requires:       python%{python3_other_pkgversion}-requests
Requires:       python%{python3_other_pkgversion}-urllib3
%endif

%description -n %{py3_other_pkgname} %{common_description}
%endif

%prep
%setup -q -c -n %{name}-%{version}

%build
%{?with_python2:%py2_build}
%{?with_python3_other:%py3_other_build}
%{?with_python3:%py3_build}

%install
%{?with_python2:%py2_install}
%{?with_python3_other:%py3_other_install}
%{?with_python3:%py3_install}

%clean
rm -rf %{buildroot}

%if %{with python2}
%files -n %{py2_pkgname}
%defattr(-,root,root,-)
%license COPYING
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}*.egg-info/
%endif

%if %{with python3}
%files -n %{py3_pkgname}
%defattr(-,root,root,-)
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info/
%endif

%if %{with python3_other}
%files -n %{py3_other_pkgname}
%defattr(-,root,root,-)
%license COPYING
%{python3_other_sitelib}/%{srcname}/
%{python3_other_sitelib}/%{srcname}*.egg-info/
%endif

%changelog
* Tue Aug 11 2020 bstinson@centosproject.org - 0.2.0-1
- Make some tweaks from python3 that handle strings better

* Wed Nov 27 2019 Jan Staněk <jstanek@redhat.com> - 0.1.1-3
- Make the code compatible with Python 3
- Modernize spec file

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


