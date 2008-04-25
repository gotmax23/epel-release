Name:           epel-release       
Version:        4 
Release:        7
Summary:        Extra Packages for Enterprise Linux repository configuration

Group:          System Environment/Base 
License:        GPL 
URL:            http://download.fedora.redhat.com/pub/epel

# This is a Fedora maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.

Source0:        http://download.fedora.redhat.com/pub/epel/RPM-GPG-KEY-EPEL
Source1:        GPL	
Source2:        epel.repo	
Source3:        epel-testing.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version} 

%description
This package contains the Extra Packages for Enterprise Linux (EPEL) repository
GPG key as well as configuration for yum and up2date.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} %{SOURCE3}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "# epel repo -- added by epel-release " \
    >> %{_sysconfdir}/sysconfig/rhn/sources
echo "yum epel http://download.fedora.redhat.com/pub/epel/%{version}/\$ARCH" \
    >> %{_sysconfdir}/sysconfig/rhn/sources

%postun 
sed -i '/^yum\ epel/d' %{_sysconfdir}/sysconfig/rhn/sources
sed -i '/^\#\ epel\ repo\ /d' %{_sysconfdir}/sysconfig/rhn/sources


%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Fri Apr 25 2008 Michael Stahnke <mastahnke@gmail.com> - 4-7
- Updated the repo file to use mirror manager for yum 

* Sun Mar 25 2007 Michael Stahnke <mastahnke@gmail.com> - 4-6
- Hard-coded '4' in yum repo files to fix string mismatch. 

* Sun Mar 25 2007 Michael Stahnke <mastahnke@gmail.com> - 4-5
- Specfile cleanup

* Sun Mar 25 2007 Michael Stahnke <mastahnke@gmail.com> - 4-4
- Changed description again

* Sun Mar 25 2007 Michael Stahnke <mastahnke@gmail.com> - 4-3
- Removed cp in postun
- Removed the file epel-release - provides no value
- Removed dist tag as per review bug #233236
- Changed description

* Mon Mar 14 2007 Michael Stahnke <mastahnke@gmail.com> - 4-2
- Fixed up2date issues. 

* Mon Mar 12 2007 Michael Stahnke <mastahnke@gmail.com> - 4-1
- Initial Package
