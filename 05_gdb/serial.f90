program hello_world_circle

implicit none
real*8 radius
real*8, external :: compute_area

radius = 1.0

write(*,*) 'radius =', radius, ' and area = ', compute_area(radius)

end program


real*8 function compute_area(r)

implicit none
real*8, intent(in) :: r
real*8, parameter :: Pi = 4.0 * atan(1.0)

compute_area = Pi * r**2

end function compute_area
